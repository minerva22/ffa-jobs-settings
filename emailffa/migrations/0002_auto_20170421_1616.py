# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailffa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='votes',
        ),
        migrations.AlterField(
            model_name='email',
            name='email_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_text',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
