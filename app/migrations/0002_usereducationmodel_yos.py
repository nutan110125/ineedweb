# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-04 09:57
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usereducationmodel',
            name='yos',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{4,5}$', 'Year must be integer')], verbose_name='Year Of Starting'),
        ),
    ]