# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 03:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('duration', models.DecimalField(decimal_places=3, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('balls_shot', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='bad_guy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bad_guy', to='api_blimp.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='good_guy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='good_guy', to='api_blimp.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='api_blimp.Player'),
        ),
    ]