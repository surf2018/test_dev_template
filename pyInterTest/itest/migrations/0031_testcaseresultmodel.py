# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itest', '0030_auto_20171023_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCaseResultModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(default=-1)),
                ('requestHead', models.TextField(default='')),
                ('requestCookie', models.TextField(default='')),
                ('requestBody', models.TextField(default='')),
                ('responseHead', models.TextField(default='')),
                ('responseCookie', models.TextField(default='')),
                ('responseBody', models.TextField(default='')),
                ('pickerValues', models.TextField(default='')),
                ('asserts', models.TextField(default='')),
                ('success', models.IntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itest.Project')),
            ],
        ),
    ]