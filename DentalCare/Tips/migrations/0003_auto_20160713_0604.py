# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-13 06:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tips', '0002_auto_20160712_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='date',
            field=models.DateField(default=datetime.date(2016, 7, 13)),
        ),
    ]
