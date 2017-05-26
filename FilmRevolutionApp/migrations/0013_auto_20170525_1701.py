# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-25 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmRevolutionApp', '0012_auto_20170521_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'FilmRevolutionApp'),
        ),
        migrations.AddField(
            model_name='director',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'FilmRevolutionApp'),
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'FilmRevolutionApp'),
        ),
        migrations.AddField(
            model_name='platform',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'FilmRevolutionApp'),
        ),
        migrations.AddField(
            model_name='production',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'FilmRevolutionApp'),
        ),
        migrations.AddField(
            model_name='serie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'FilmRevolutionApp'),
        ),
    ]