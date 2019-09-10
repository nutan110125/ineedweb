# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-20 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_content_management', '0002_termsandconditions'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True, verbose_name='Question')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Answer')),
            ],
            options={
                'verbose_name_plural': 'FAQ',
            },
        ),
    ]
