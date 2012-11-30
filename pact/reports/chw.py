from datetime import datetime
import pdb
from django.http import Http404
import simplejson
from casexml.apps.case.models import CommCareCase
from corehq.apps.api.xform_es import XFormES
from corehq.apps.reports.datatables import DataTablesHeader, DataTablesColumn
from corehq.apps.reports.dispatcher import ProjectReportDispatcher, CustomProjectReportDispatcher
from corehq.apps.reports.generic import GenericTabularReport
from corehq.apps.reports.standard import CustomProjectReport
from corehq.apps.users.models import CommCareUser
from dimagi.utils.decorators.memoized import memoized
from pact.models import CDotWeeklySchedule, PactPatientCase
from pact.reports import PactPatientDispatcher, PactDrilldownReportMixin, PatientNavigationReport


class PactCHWProfileReport(PactDrilldownReportMixin, GenericTabularReport, CustomProjectReport):
    slug = "chw_profile"
    description = "CHW Profile"
    view_mode='info'
    ajax_pagination = True
    xform_es = XFormES()

    hide_filters = True
    filters = []
#    fields = ['corehq.apps.reports.fields.FilterUsersField', 'corehq.apps.reports.fields.DatespanField',]
#    hide_filters=False

    def get_fields(self):
        if self.view_mode == 'submissions':
            yield 'corehq.apps.reports.fields.FilterUsersField'
            yield 'corehq.apps.reports.fields.DatespanField'


    @memoized
    def get_user(self):
        if hasattr(self, 'request') and self.request.GET.has_key('chw_id'):
            self._user_doc = CommCareUser.get(self.request.GET['chw_id'])
            return self._user_doc
        else:
            return None


    @property
    def name(self):
        if hasattr(self, 'request') and self.request.GET.has_key('chw_id'):
            return "CHW Profile :: %s" % self.get_user().raw_username
        else:
            return "CHW Profile"


    @property
    def report_context(self):
        user_doc = self.get_user()
        self.view_mode = self.request.GET.get('view', 'info')
        ret = {'user_doc': user_doc}
        ret['view_mode'] = self.view_mode
        ret['chw_root_url'] = PactCHWProfileReport.get_url(*[self.request.domain]) + "?chw_id=%s" % self.request.GET['chw_id']
        print self.request.GET.keys()

        if self.view_mode == 'info':
            self.hide_filters=True
            self.report_template_path = "pact/chw/pact_chw_profile_info.html"
        elif self.view_mode == 'submissions':
            tabular_context = super(PactCHWProfileReport, self).report_context
            tabular_context.update(ret)
            self.report_template_path = "pact/chw/pact_chw_profile_submissions.html"
            return tabular_context
        elif self.view_mode == 'schedule':
            self.report_template_path = "pact/chw/pact_chw_profile_schedule.html"
        else:
            raise Http404
        return ret



    #submission stuff
    @property
    def headers(self):
        return DataTablesHeader(DataTablesColumn("Pact ID"),
#                                DataTablesColumn("Patient Name"),
                                DataTablesColumn("Form"),
                                DataTablesColumn("Encounter Date"),
                                DataTablesColumn("Received"),
        )

    @property
    @memoized
    def es_results(self):
        user = self.get_user()
        query = self.xform_es.base_query(self.request.domain, start=self.pagination.start, size=self.pagination.count)
        query['fields'] = [
                            "form.#type",
                            "form.encounter_date",
                            "form.note.encounter_date",
                            "form.case.case_id",
                            "form.case.@case_id",
                            "form.pact_id",
                            "form.note.pact_id",
                            "received_on",
                            "form.meta.timeStart",
                            "form.meta.timeEnd"
                        ]
        query['filter']['and'].append({"term": {"form.meta.username": user.raw_username}})
        return self.xform_es.run_query(query)

    @property
    def rows(self):
        """
            Override this method to create a functional tabular report.
            Returns 2D list of rows.
            [['row1'],[row2']]
        """
        if self.get_user() is not None:
            rows = []
            def _format_row(row_field_dict):
                for p in ["form.pact_id", "form.note.pact_id", None]:
                    if p is None:
                        yield ""
                    if row_field_dict.has_key(p):
                        yield row_field_dict[p]
                        break
                yield row_field_dict["form.#type"].replace('_', ' ').title()
                for p in ["form.encounter_date", "form.note.encounter_date", None]:
                    if p is None:
                        yield "None"
                    if row_field_dict.has_key(p):
                        yield row_field_dict[p]
                        break
                yield row_field_dict["received_on"].replace('_', ' ').title()

            res = self.es_results
            print simplejson.dumps(res.keys(), indent=4)
            if res.has_key('error'):
                pass
            else:
                for result in res['hits']['hits']:
                    yield list(_format_row(result['fields']))

    @property
    def total_records(self):
        """
            Override for pagination.
            Returns an integer.
        """
        res = self.es_results
        return res['hits'].get('total', 0)

    @property
    def total_filtered_records(self):
        """
            Override for pagination.
            Returns an integer.
            return -1 if you want total_filtered_records to equal whatever the value of total_records is.
        """
        return -1

    @property
    def shared_pagination_GET_params(self):
        """
            Override.
            Should return a list of dicts with the name and value of the GET parameters
            that you'd like to pass to the server-side pagination.
            ex: [dict(name='group', value=self.group_name)]
        """
        ret = []
        for k,v in self.request.GET.items():
            ret.append(dict(name=k, value=v))
        return ret

    def per_case_submissions_facet(self):
        user=self.get_user()
        query = {
            "facets": {
                "case_submissions": {
                    "terms": {
                        "field": "form.case.case_id"
                    },
                    "facet_filter": {
                        "and": [
                            {
                                "term": {
                                    "domain.exact": "pact"
                                }
                            },
                            {
                                "term": {
                                    "form.meta.username": user.raw_username
                                }
                            }
                        ]
                    }
                }
            },
            #            "sort": {
            #                "received_on": "desc"
            #            },
            "size": 0
        }

    def my_submissions(self):
        user=self.get_user()
        query = {
            "fields": [
                "form.#type",
                "form.encounter_date",
                "form.note.encounter_date",
                "form.case.case_id",
                "form.case.@case_id",
                "received_on",
                "form.meta.timeStart",
                "form.meta.timeEnd"
            ],
            "filter": {
                "and": [
                    {
                        "term": {
                            "domain.exact": "pact"
                        }
                    },
                    {
                        "term": {
                            "form.meta.username": user.raw_username
                        }
                    }
                ]
            },
            "sort": {
                "received_on": "desc"
            },
            "size": 10,
            "from": 0
        }


