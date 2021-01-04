# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-22 12:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment_report', '0031_auto_20201020_1027'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AlterModelOptions(
            name='killerfacts',
            options={'verbose_name': '2 - Achieving Great Things in Sector', 'verbose_name_plural': '2 - Achieving Great Things in Sector'},
        ),
        migrations.AlterModelOptions(
            name='lastpage',
            options={'verbose_name': '9 - Last Page', 'verbose_name_plural': '9 - Last Page'},
        ),
        migrations.AlterModelOptions(
            name='macrocontextbetweencountries',
            options={'verbose_name': '3 - Links that are already strong', 'verbose_name_plural': '3 - Links that are already strong'},
        ),
        migrations.AlterModelOptions(
            name='sectorinitiatives',
            options={'verbose_name': '6 - Sector in the UK', 'verbose_name_plural': '6 - Sector in the UK'},
        ),
        migrations.AlterModelOptions(
            name='sectoroverview',
            options={'verbose_name': '1 - A Great Home for Company', 'verbose_name_plural': '1 - A Great Home for Company'},
        ),
    ]