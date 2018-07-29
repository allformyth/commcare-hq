# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-29 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0034_remove_subscription_date_delay_invoicing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaccount',
            name='auto_pay_user',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='billingaccount',
            name='created_by',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='subscriptionadjustment',
            name='method',
            field=models.CharField(choices=[('USER', 'User'), ('INTERNAL', 'Ops'), ('TASK', '[Deprecated] Task (Invoicing)'), ('TRIAL', '30 Day Trial'), ('AUTOMATIC_DOWNGRADE', 'Automatic Downgrade'), ('DEFAULT_COMMUNITY', 'Default to Community'), ('INVOICING', 'Invoicing')], default='INTERNAL', max_length=50),
        ),
    ]
