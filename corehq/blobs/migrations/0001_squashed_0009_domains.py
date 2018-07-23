# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-20 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('blobs', '0001_initial'), ('blobs', '0002_auto_20151221_1623'), ('blobs', '0003_auto_20161012_1358'), ('blobs', '0004_auto_20170321_1956'), ('blobs', '0005_blobexpiration'), ('blobs', '0006_auto_20170821_1826'), ('blobs', '0007_invoicepdf'), ('blobs', '0008_commcare_builds'), ('blobs', '0009_domains')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlobMigrationState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=20, unique=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlobExpiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket', models.CharField(max_length=255)),
                ('identifier', models.CharField(db_index=True, max_length=255)),
                ('expires_on', models.DateTimeField(db_index=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('length', models.IntegerField()),
                ('deleted', models.BooleanField(db_index=True, default=False)),
            ],
        ),
    ]