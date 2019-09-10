# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-13 04:36
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0027_auto_20190708_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.EmailField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\\.[a-zA-Z]+$', 'Email must contain at least one @ and .')], verbose_name='Reciver')),
                ('url', models.URLField(verbose_name='Url of site')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_referer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Refer User',
            },
        ),
        migrations.AlterModelOptions(
            name='contactusmodel',
            options={'verbose_name_plural': 'Post Contact Us'},
        ),
    ]
