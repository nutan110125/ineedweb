# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-22 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_content_management', '0007_career'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='resume',
            field=models.URLField(blank=True, null=True, verbose_name='Resume'),
        ),
    ]
