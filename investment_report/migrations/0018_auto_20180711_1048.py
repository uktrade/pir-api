# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-11 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_report', '0017_pirrequest_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='pirrequest',
            name='phone_number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
