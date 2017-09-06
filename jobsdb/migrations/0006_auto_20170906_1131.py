# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-06 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsdb', '0005_auto_20170829_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='isdefault',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(choices=[('beirut', 'BEIRUT'), ('bsalim', 'BSALIM'), ('test', 'TEST')], max_length=10),
        ),
    ]
