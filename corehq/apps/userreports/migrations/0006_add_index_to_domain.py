# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-05 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userreports', '0005_asyncindicator_unsuccessful_attempts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asyncindicator',
            name='domain',
            field=models.CharField(db_index=True, max_length=126),
        ),
    ]
