# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-07 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_report', '0016_auto_20180525_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='pirrequest',
            name='lang',
            field=models.CharField(default='en', max_length=255),
        ),
    ]
