# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-25 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('investment_report', '0015_pirrequest_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pirrequest',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='countries_plus.Country'),
        ),
    ]
