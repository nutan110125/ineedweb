# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-21 12:39
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '__first__'),
        ('static_content_management', '0006_privacypolicy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='User Email')),
                ('first_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Last Name')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Mobile Number')),
                ('resume', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Resume')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrer_profession', to='app.Profession')),
            ],
            options={
                'verbose_name_plural': 'Careers',
            },
        ),
    ]