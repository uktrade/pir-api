# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-31 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_report', '0022_killerfacts_background_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='macrocontextbetweencountries',
            name='background_image',
            field=models.ImageField(blank=True, help_text='Background image for this page', null=True, upload_to=''),
        ),
    ]