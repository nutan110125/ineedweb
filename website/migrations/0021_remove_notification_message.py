# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-01 05:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_notification_type_of_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='message',
        ),
    ]
