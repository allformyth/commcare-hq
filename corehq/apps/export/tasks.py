from celery.task import task

from corehq.apps.export.export import get_export_file
from couchexport.models import Format
from couchexport.tasks import escape_quotes
from soil.util import expose_cached_download


@task
def get_export_download(export_instances, filters, download_id, filename=None, expiry=10*60*60):
    export_file = get_export_file(export_instances, filters)

    format = Format.from_format(export_file.format)
    filename = filename or export_instances[0].name
    escaped_filename = escape_quotes('%s.%s' % (filename, format.extension))

    payload = export_file.file.payload
    expose_cached_download(
        payload,
        expiry,
        ".{}".format(format.extension),
        mimetype=format.mimetype,
        content_disposition='attachment; filename="%s"' % escaped_filename,
        download_id=download_id,
    )
    export_file.file.delete()
