from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models


class AggAwcDailyView(models.Model):
    awc_id = models.TextField(primary_key=True)
    awc_name = models.TextField(blank=True, null=True)
    awc_site_code = models.TextField(blank=True, null=True)
    supervisor_id = models.TextField(blank=True, null=True)
    supervisor_name = models.TextField(blank=True, null=True)
    supervisor_site_code = models.TextField(blank=True, null=True)
    block_id = models.TextField(blank=True, null=True)
    block_name = models.TextField(blank=True, null=True)
    block_site_code = models.TextField(blank=True, null=True)
    district_id = models.TextField(blank=True, null=True)
    district_name = models.TextField(blank=True, null=True)
    district_site_code = models.TextField(blank=True, null=True)
    state_id = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    state_site_code = models.TextField(blank=True, null=True)
    block_map_location_name = models.TextField(blank=True, null=True)
    district_map_location_name = models.TextField(blank=True, null=True)
    state_map_location_name = models.TextField(blank=True, null=True)
    aggregation_level = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    cases_household = models.IntegerField(blank=True, null=True)
    cases_person = models.IntegerField(blank=True, null=True)
    cases_person_all = models.IntegerField(blank=True, null=True)
    cases_person_has_aadhaar = models.IntegerField(blank=True, null=True)
    cases_person_beneficiary = models.IntegerField(blank=True, null=True)
    cases_person_adolescent_girls_11_14 = models.IntegerField(blank=True, null=True)
    cases_person_adolescent_girls_15_18 = models.IntegerField(blank=True, null=True)
    cases_person_adolescent_girls_11_14_all = models.IntegerField(blank=True, null=True)
    cases_person_adolescent_girls_15_18_all = models.IntegerField(blank=True, null=True)
    cases_ccs_pregnant = models.IntegerField(blank=True, null=True)
    cases_ccs_lactating = models.IntegerField(blank=True, null=True)
    cases_child_health = models.IntegerField(blank=True, null=True)
    cases_ccs_pregnant_all = models.IntegerField(blank=True, null=True)
    cases_ccs_lactating_all = models.IntegerField(blank=True, null=True)
    cases_child_health_all = models.IntegerField(blank=True, null=True)
    daily_attendance_open = models.IntegerField(blank=True, null=True)
    num_awcs = models.IntegerField(blank=True, null=True)
    num_launched_states = models.IntegerField(blank=True, null=True)
    num_launched_districts = models.IntegerField(blank=True, null=True)
    num_launched_blocks = models.IntegerField(blank=True, null=True)
    num_launched_supervisors = models.IntegerField(blank=True, null=True)
    num_launched_awcs = models.IntegerField(blank=True, null=True)
    cases_person_has_aadhaar_v2 = models.IntegerField(blank=True, null=True)
    cases_person_beneficiary_v2 = models.IntegerField(blank=True, null=True)

    class Meta(object):
        app_label = 'icds_model'
        managed = False
        db_table = 'agg_awc_daily_view'


class DailyAttendanceView(models.Model):
    awc_id = models.TextField(primary_key=True)
    awc_name = models.TextField(blank=True, null=True)
    awc_site_code = models.TextField(blank=True, null=True)
    supervisor_id = models.TextField(blank=True, null=True)
    supervisor_name = models.TextField(blank=True, null=True)
    supervisor_site_code = models.TextField(blank=True, null=True)
    block_id = models.TextField(blank=True, null=True)
    block_name = models.TextField(blank=True, null=True)
    block_site_code = models.TextField(blank=True, null=True)
    district_id = models.TextField(blank=True, null=True)
    district_name = models.TextField(blank=True, null=True)
    district_site_code = models.TextField(blank=True, null=True)
    state_id = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    state_site_code = models.TextField(blank=True, null=True)
    aggregation_level = models.IntegerField(blank=True, null=True)
    block_map_location_name = models.TextField(blank=True, null=True)
    district_map_location_name = models.TextField(blank=True, null=True)
    state_map_location_name = models.TextField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    doc_id = models.TextField(blank=True, null=True)
    pse_date = models.DateField(blank=True, null=True)
    awc_open_count = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    eligible_children = models.IntegerField(blank=True, null=True)
    attended_children = models.IntegerField(blank=True, null=True)
    attended_children_percent = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    form_location = models.TextField(blank=True, null=True)
    form_location_lat = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    form_location_long = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    image_name = models.TextField(blank=True, null=True)

    class Meta(object):
        app_label = 'icds_model'
        managed = False
        db_table = 'daily_attendance_view'


class ChildHealthMonthlyView(models.Model):
    case_id = models.TextField(primary_key=True)
    awc_id = models.TextField(blank=True, null=True)
    supervisor_id = models.TextField(blank=True, null=True)
    block_id = models.TextField(blank=True, null=True)
    district_id = models.TextField(blank=True, null=True)
    state_id = models.TextField(blank=True, null=True)
    person_name = models.TextField(blank=True, null=True)
    mother_name = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    age_in_months = models.IntegerField(blank=True, null=True)
    open_in_month = models.IntegerField(blank=True, null=True)
    valid_in_month = models.IntegerField(blank=True, null=True)
    nutrition_status_last_recorded = models.TextField(blank=True, null=True)
    current_month_nutrition_status = models.TextField(blank=True, null=True)
    pse_days_attended = models.IntegerField(blank=True, null=True)
    recorded_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    recorded_height = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    thr_eligible = models.IntegerField(blank=True, null=True)
    current_month_stunting = models.TextField(blank=True, null=True)
    current_month_wasting = models.TextField(blank=True, null=True)
    fully_immunized = models.IntegerField(blank=True, null=True)
    current_month_nutrition_status_sort = models.IntegerField(blank=True, null=True)
    current_month_stunting_sort = models.IntegerField(blank=True, null=True)
    current_month_wasting_sort = models.IntegerField(blank=True, null=True)
    current_month_stunting_v2 = models.TextField(blank=True, null=True)
    current_month_wasting_v2 = models.TextField(blank=True, null=True)
    current_month_stunting_v2_sort = models.IntegerField(blank=True, null=True)
    current_month_wasting_v2_sort = models.IntegerField(blank=True, null=True)

    class Meta(object):
        app_label = 'icds_model'
        managed = False
        db_table = 'child_health_monthly_view'


class AggAwcMonthly(models.Model):
    awc_id = models.TextField(primary_key=True)
    awc_name = models.TextField(blank=True, null=True)
    awc_site_code = models.TextField(blank=True, null=True)
    supervisor_id = models.TextField(blank=True, null=True)
    supervisor_name = models.TextField(blank=True, null=True)
    supervisor_site_code = models.TextField(blank=True, null=True)
    block_id = models.TextField(blank=True, null=True)
    block_name = models.TextField(blank=True, null=True)
    block_site_code = models.TextField(blank=True, null=True)
    district_id = models.TextField(blank=True, null=True)
    district_name = models.TextField(blank=True, null=True)
    district_site_code = models.TextField(blank=True, null=True)
    state_id = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    state_site_code = models.TextField(blank=True, null=True)
    aggregation_level = models.IntegerField(blank=True, null=True)
    block_map_location_name = models.TextField(blank=True, null=True)
    district_map_location_name = models.TextField(blank=True, null=True)
    state_map_location_name = models.TextField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    aww_name = models.TextField(blank=True, null=True)
    contact_phone_number = models.TextField(blank=True, null=True)
    num_awcs = models.IntegerField(blank=True, null=True)
    num_launched_states = models.IntegerField(blank=True, null=True)
    num_launched_districts = models.IntegerField(blank=True, null=True)
    num_launched_blocks = models.IntegerField(blank=True, null=True)
    num_launched_supervisors = models.IntegerField(blank=True, null=True)
    num_launched_awcs = models.IntegerField(blank=True, null=True)
    awc_days_open = models.IntegerField(blank=True, null=True)
    awc_days_pse_conducted = models.IntegerField(blank=True, null=True)
    awc_num_open = models.IntegerField(blank=True, null=True)
    wer_weighed = models.IntegerField(blank=True, null=True)
    wer_eligible = models.IntegerField(blank=True, null=True)
    num_anc_visits = models.IntegerField(blank=True, null=True)
    num_children_immunized = models.IntegerField(blank=True, null=True)
    cases_household = models.IntegerField(blank=True, null=True)
    cases_person = models.IntegerField(blank=True, null=True)
    cases_person_all = models.IntegerField(blank=True, null=True)
    cases_person_has_aadhaar = models.IntegerField(blank=True, null=True)
    cases_person_beneficiary = models.IntegerField(blank=True, null=True)
    cases_person_adolescent_girls_11_14 = models.IntegerField(blank=True, null=True)
    cases_person_adolescent_girls_15_18 = models.IntegerField(blank=True, null=True)
    cases_person_adolescent_girls_11_14_all = models.IntegerField(blank=True, null=True)
    cases_person_adolescent_girls_15_18_all = models.IntegerField(blank=True, null=True)
    cases_person_referred = models.IntegerField(blank=True, null=True)
    cases_ccs_pregnant = models.IntegerField(blank=True, null=True)
    cases_ccs_lactating = models.IntegerField(blank=True, null=True)
    cases_child_health = models.IntegerField(blank=True, null=True)
    cases_ccs_pregnant_all = models.IntegerField(blank=True, null=True)
    cases_ccs_lactating_all = models.IntegerField(blank=True, null=True)
    cases_child_health_all = models.IntegerField(blank=True, null=True)
    usage_num_pse = models.IntegerField(blank=True, null=True)
    usage_num_gmp = models.IntegerField(blank=True, null=True)
    usage_num_thr = models.IntegerField(blank=True, null=True)
    usage_num_home_visit = models.IntegerField(blank=True, null=True)
    usage_num_bp_tri1 = models.IntegerField(blank=True, null=True)
    usage_num_bp_tri2 = models.IntegerField(blank=True, null=True)
    usage_num_bp_tri3 = models.IntegerField(blank=True, null=True)
    usage_num_pnc = models.IntegerField(blank=True, null=True)
    usage_num_ebf = models.IntegerField(blank=True, null=True)
    usage_num_cf = models.IntegerField(blank=True, null=True)
    usage_num_delivery = models.IntegerField(blank=True, null=True)
    usage_num_due_list_ccs = models.IntegerField(blank=True, null=True)
    usage_num_due_list_child_health = models.IntegerField(blank=True, null=True)
    infra_type_of_building = models.TextField(blank=True, null=True)
    infra_clean_water = models.IntegerField(blank=True, null=True)
    infra_functional_toilet = models.IntegerField(blank=True, null=True)
    infra_adult_weighing_scale = models.IntegerField(blank=True, null=True)
    infra_infant_weighing_scale = models.IntegerField(blank=True, null=True)
    infra_medicine_kits = models.IntegerField(blank=True, null=True)
    num_awc_infra_last_update = models.IntegerField(blank=True, null=True)
    usage_num_hh_reg = models.IntegerField(blank=True, null=True)
    usage_num_add_pregnancy = models.IntegerField(blank=True, null=True)
    cases_person_has_aadhaar_v2 = models.IntegerField(blank=True, null=True)
    cases_person_beneficiary_v2 = models.IntegerField(blank=True, null=True)

    class Meta(object):
        app_label = 'icds_model'
        managed = False
        db_table = 'agg_awc_monthly'


class AggCcsRecordMonthly(models.Model):
    awc_id = models.TextField(primary_key=True)
    awc_name = models.TextField(blank=True, null=True)
    awc_site_code = models.TextField(blank=True, null=True)
    supervisor_id = models.TextField(blank=True, null=True)
    supervisor_name = models.TextField(blank=True, null=True)
    supervisor_site_code = models.TextField(blank=True, null=True)
    block_id = models.TextField(blank=True, null=True)
    block_name = models.TextField(blank=True, null=True)
    block_site_code = models.TextField(blank=True, null=True)
    district_id = models.TextField(blank=True, null=True)
    district_name = models.TextField(blank=True, null=True)
    district_site_code = models.TextField(blank=True, null=True)
    state_id = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    state_site_code = models.TextField(blank=True, null=True)
    aggregation_level = models.IntegerField(blank=True, null=True)
    block_map_location_name = models.TextField(blank=True, null=True)
    district_map_location_name = models.TextField(blank=True, null=True)
    state_map_location_name = models.TextField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    ccs_status = models.TextField(blank=True, null=True)
    trimester = models.TextField(blank=True, null=True)
    caste = models.TextField(blank=True, null=True)
    disabled = models.TextField(blank=True, null=True)
    minority = models.TextField(blank=True, null=True)
    resident = models.TextField(blank=True, null=True)
    valid_in_month = models.IntegerField(blank=True, null=True)
    valid_all_registered_in_month = models.IntegerField(blank=True, null=True)
    lactating = models.IntegerField(blank=True, null=True)
    pregnant = models.IntegerField(blank=True, null=True)
    lactating_all = models.IntegerField(blank=True, null=True)
    pregnant_all = models.IntegerField(blank=True, null=True)
    thr_eligible = models.IntegerField(blank=True, null=True)
    rations_21_plus_distributed = models.IntegerField(blank=True, null=True)
    tetanus_complete = models.IntegerField(blank=True, null=True)
    delivered_in_month = models.IntegerField(blank=True, null=True)
    anc1_received_at_delivery = models.IntegerField(blank=True, null=True)
    anc2_received_at_delivery = models.IntegerField(blank=True, null=True)
    anc3_received_at_delivery = models.IntegerField(blank=True, null=True)
    anc4_received_at_delivery = models.IntegerField(blank=True, null=True)
    registration_trimester_at_delivery = models.DecimalField(
        max_digits=65535,
        decimal_places=65535,
        blank=True,
        null=True
    )
    institutional_delivery_in_month = models.IntegerField(blank=True, null=True)
    using_ifa = models.IntegerField(blank=True, null=True)
    ifa_consumed_last_seven_days = models.IntegerField(blank=True, null=True)
    anemic_normal = models.IntegerField(blank=True, null=True)
    anemic_moderate = models.IntegerField(blank=True, null=True)
    anemic_severe = models.IntegerField(blank=True, null=True)
    anemic_unknown = models.IntegerField(blank=True, null=True)
    extra_meal = models.IntegerField(blank=True, null=True)
    resting_during_pregnancy = models.IntegerField(blank=True, null=True)
    bp1_complete = models.IntegerField(blank=True, null=True)
    bp2_complete = models.IntegerField(blank=True, null=True)
    bp3_complete = models.IntegerField(blank=True, null=True)
    pnc_complete = models.IntegerField(blank=True, null=True)
    trimester_2 = models.IntegerField(blank=True, null=True)
    trimester_3 = models.IntegerField(blank=True, null=True)
    postnatal = models.IntegerField(blank=True, null=True)
    counsel_bp_vid = models.IntegerField(blank=True, null=True)
    counsel_preparation = models.IntegerField(blank=True, null=True)
    counsel_immediate_bf = models.IntegerField(blank=True, null=True)
    counsel_fp_vid = models.IntegerField(blank=True, null=True)
    counsel_immediate_conception = models.IntegerField(blank=True, null=True)
    counsel_accessible_postpartum_fp = models.IntegerField(blank=True, null=True)

    class Meta(object):
        app_label = 'icds_model'
        managed = False
        db_table = 'agg_ccs_record_monthly'


class AggChildHealthMonthly(models.Model):
    awc_id = models.TextField(primary_key=True)
    awc_name = models.TextField(blank=True, null=True)
    awc_site_code = models.TextField(blank=True, null=True)
    supervisor_id = models.TextField(blank=True, null=True)
    supervisor_name = models.TextField(blank=True, null=True)
    supervisor_site_code = models.TextField(blank=True, null=True)
    block_id = models.TextField(blank=True, null=True)
    block_name = models.TextField(blank=True, null=True)
    block_site_code = models.TextField(blank=True, null=True)
    district_id = models.TextField(blank=True, null=True)
    district_name = models.TextField(blank=True, null=True)
    district_site_code = models.TextField(blank=True, null=True)
    state_id = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    state_site_code = models.TextField(blank=True, null=True)
    block_map_location_name = models.TextField(blank=True, null=True)
    district_map_location_name = models.TextField(blank=True, null=True)
    state_map_location_name = models.TextField(blank=True, null=True)
    aggregation_level = models.IntegerField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    month_display = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    age_tranche = models.TextField(blank=True, null=True)
    caste = models.TextField(blank=True, null=True)
    disabled = models.TextField(blank=True, null=True)
    minority = models.TextField(blank=True, null=True)
    resident = models.TextField(blank=True, null=True)
    valid_in_month = models.IntegerField(blank=True, null=True)
    valid_all_registered_in_month = models.IntegerField(blank=True, null=True)
    nutrition_status_weighed = models.IntegerField(blank=True, null=True)
    nutrition_status_unweighed = models.IntegerField(blank=True, null=True)
    nutrition_status_normal = models.IntegerField(blank=True, null=True)
    nutrition_status_moderately_underweight = models.IntegerField(blank=True, null=True)
    nutrition_status_severely_underweight = models.IntegerField(blank=True, null=True)
    wer_eligible = models.IntegerField(blank=True, null=True)
    height_measured_in_month = models.IntegerField(blank=True, null=True)
    height_eligible = models.IntegerField(blank=True, null=True)
    wasting_moderate = models.IntegerField(blank=True, null=True)
    wasting_severe = models.IntegerField(blank=True, null=True)
    wasting_normal = models.IntegerField(blank=True, null=True)
    wasting_moderate_v2 = models.IntegerField(blank=True, null=True)
    wasting_severe_v2 = models.IntegerField(blank=True, null=True)
    wasting_normal_v2 = models.IntegerField(blank=True, null=True)
    stunting_moderate = models.IntegerField(blank=True, null=True)
    stunting_severe = models.IntegerField(blank=True, null=True)
    stunting_normal = models.IntegerField(blank=True, null=True)
    zscore_grading_hfa_moderate = models.IntegerField(blank=True, null=True)
    zscore_grading_hfa_severe = models.IntegerField(blank=True, null=True)
    zscore_grading_hfa_normal = models.IntegerField(blank=True, null=True)
    pnc_eligible = models.IntegerField(blank=True, null=True)
    thr_eligible = models.IntegerField(blank=True, null=True)
    rations_21_plus_distributed = models.IntegerField(blank=True, null=True)
    pse_eligible = models.IntegerField(blank=True, null=True)
    pse_attended_16_days = models.IntegerField(blank=True, null=True)
    born_in_month = models.IntegerField(blank=True, null=True)
    low_birth_weight_in_month = models.IntegerField(blank=True, null=True)
    bf_at_birth = models.IntegerField(blank=True, null=True)
    ebf_eligible = models.IntegerField(blank=True, null=True)
    ebf_in_month = models.IntegerField(blank=True, null=True)
    ebf_no_info_recorded = models.IntegerField(blank=True, null=True)
    cf_initiation_in_month = models.IntegerField(blank=True, null=True)
    cf_initiation_eligible = models.IntegerField(blank=True, null=True)
    cf_eligible = models.IntegerField(blank=True, null=True)
    cf_in_month = models.IntegerField(blank=True, null=True)
    cf_diet_diversity = models.IntegerField(blank=True, null=True)
    cf_diet_quantity = models.IntegerField(blank=True, null=True)
    cf_demo = models.IntegerField(blank=True, null=True)
    cf_handwashing = models.IntegerField(blank=True, null=True)
    counsel_increase_food_bf = models.IntegerField(blank=True, null=True)
    counsel_manage_breast_problems = models.IntegerField(blank=True, null=True)
    counsel_ebf = models.IntegerField(blank=True, null=True)
    counsel_adequate_bf = models.IntegerField(blank=True, null=True)
    counsel_pediatric_ifa = models.IntegerField(blank=True, null=True)
    counsel_play_cf_video = models.IntegerField(blank=True, null=True)
    fully_immunized_eligible = models.IntegerField(blank=True, null=True)
    fully_immunized_on_time = models.IntegerField(blank=True, null=True)
    fully_immunized_late = models.IntegerField(blank=True, null=True)
    weighed_and_height_measured_in_month = models.IntegerField(blank=True, null=True)
    weighed_and_born_in_month = models.IntegerField(blank=True, null=True)
    days_ration_given_child = models.IntegerField(blank=True, null=True)

    class Meta(object):
        app_label = 'icds_model'
        managed = False
        db_table = 'agg_child_health_monthly'


class AwcLocationMonths(models.Model):
    awc_id = models.TextField(primary_key=True)
    awc_name = models.TextField(blank=True, null=True)
    awc_site_code = models.TextField(blank=True, null=True)
    supervisor_id = models.TextField(blank=True, null=True)
    supervisor_name = models.TextField(blank=True, null=True)
    supervisor_site_code = models.TextField(blank=True, null=True)
    block_id = models.TextField(blank=True, null=True)
    block_name = models.TextField(blank=True, null=True)
    block_site_code = models.TextField(blank=True, null=True)
    district_id = models.TextField(blank=True, null=True)
    district_name = models.TextField(blank=True, null=True)
    district_site_code = models.TextField(blank=True, null=True)
    state_id = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    state_site_code = models.TextField(blank=True, null=True)
    aggregation_level = models.IntegerField(blank=True, null=True)
    block_map_location_name = models.TextField(blank=True, null=True)
    district_map_location_name = models.TextField(blank=True, null=True)
    state_map_location_name = models.TextField(blank=True, null=True)
    month = models.DateField(blank=True, null=True)
    month_display = models.TextField(blank=True, null=True)
    aww_name = models.TextField(blank=True, null=True)
    contact_phone_number = models.TextField(blank=True, null=True)

    class Meta(object):
        app_label = 'icds_model'
        managed = False
        db_table = 'awc_location_months'

