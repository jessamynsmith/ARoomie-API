# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-10 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aroomieapp', '0008_auto_20161210_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender_pref',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], default=-1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='race',
            field=models.IntegerField(choices=[(1, 'Malay'), (2, 'Chinese'), (3, 'Indian'), (4, 'Others')], default=-1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='race_pref',
            field=models.IntegerField(choices=[(1, 'Malay'), (2, 'Chinese'), (3, 'Indian'), (4, 'Others')], default=-1),
        ),
    ]