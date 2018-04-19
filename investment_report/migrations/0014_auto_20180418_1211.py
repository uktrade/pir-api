# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-18 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_report', '0013_whoishere'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='display_name',
            field=models.CharField(default='Tech', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sector',
            name='display_name_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='display_name_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='display_name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='display_name_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='display_name_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='display_name_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='display_name_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='display_name_zh_cn',
            field=models.CharField(max_length=255, null=True),
        ),
    ]