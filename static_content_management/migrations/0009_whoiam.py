# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-12 05:43
from __future__ import unicode_literals

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('static_content_management', '0008_auto_20190622_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoIAm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', djrichtextfield.models.RichTextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Who I am',
            },
        ),
    ]
