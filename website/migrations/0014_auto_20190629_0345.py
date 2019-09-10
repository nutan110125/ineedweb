# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-29 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_chatmodel_is_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapplyjob',
            name='employer_is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userapplyjob',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userapplyjob',
            name='job_seeker_is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
