# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-22 10:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qna_app', '0013_auto_20180222_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='user',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]
