# Generated by Django 2.1.7 on 2019-06-20 07:09

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('static_content_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndConditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title')),
                ('description', djrichtextfield.models.RichTextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Terms And Condition',
            },
        ),
    ]