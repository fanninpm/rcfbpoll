# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2020-09-26 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0015_auto_20160829_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('name',)},
        ),
    ]
