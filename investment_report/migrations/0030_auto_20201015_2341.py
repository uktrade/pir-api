# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-15 23:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment_report', '0029_casestudysector_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rdandinnovationcasestudy',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='videocasestudy',
            name='sector',
        ),
        migrations.DeleteModel(
            name='WhoIsHere',
        ),
        migrations.DeleteModel(
            name='RDandInnovationCaseStudy',
        ),
        migrations.DeleteModel(
            name='VideoCaseStudy',
        ),
    ]
