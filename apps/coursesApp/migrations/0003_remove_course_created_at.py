# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 02:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursesApp', '0002_auto_20170222_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='created_at',
        ),
    ]
