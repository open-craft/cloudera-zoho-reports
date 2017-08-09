# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.SlugField(help_text='The URL path the page will be available at.', max_length=255, verbose_name='URL path')),
                ('html', models.TextField(help_text='The HTML source code of the page.', verbose_name='Page source')),
                ('_allowed_emails', models.CharField(blank=True, db_column='allowed_users', help_text='Comma-seprateed list of email addresses with access to the page', max_length=511, verbose_name='Allowed users')),
            ],
        ),
    ]