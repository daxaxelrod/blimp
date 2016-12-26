# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_blimp', '0002_auto_20161226_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='good_guy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='good_guy', to='api_blimp.Player'),
        ),
    ]