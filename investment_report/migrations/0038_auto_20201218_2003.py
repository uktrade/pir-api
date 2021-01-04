# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-18 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_report', '0037_marketcontact_first_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketcontact',
            name='contact_display_link',
            field=models.CharField(blank=True, help_text='The contact url display', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='marketcontact',
            name='contact_url',
            field=models.CharField(blank=True, help_text='The actual contact page url', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='marketcontact',
            name='title',
            field=models.CharField(blank=True, help_text='Title appearing in any other contact box besides the first', max_length=250, null=True),
        ),
    ]