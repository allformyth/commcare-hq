# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import migrations

from corehq.sql_db.operations import RawSQLMigration

migrator = RawSQLMigration(('corehq', 'sql_accessors', 'sql_templates'), {})


class Migration(migrations.Migration):

    dependencies = [
        ('sql_accessors', '0008_get_case_by_external_id'),
        ('form_processor', '0039_auto_20151130_1748'),
    ]

    operations = [
        migrator.get_migration('get_ledger_value.sql'),
    ]
