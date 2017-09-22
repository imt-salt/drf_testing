# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-20 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liability', models.BooleanField(default=False)),
                ('coverage_type', models.CharField(max_length=140)),
            ],
        ),
    ]