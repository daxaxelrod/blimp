# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 08:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_blimp', '0004_auto_20161226_0657'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='game',
            unique_together=set([('good_guy', 'bad_guy')]),
        ),
    ]
