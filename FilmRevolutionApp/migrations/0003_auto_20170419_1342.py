# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 13:42
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FilmRevolutionApp', '0002_seriereview'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ActorM', to='FilmRevolutionApp.Movie'),
        ),
        migrations.AddField(
            model_name='actor',
            name='serie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ActorS', to='FilmRevolutionApp.Serie'),
        ),
        migrations.AddField(
            model_name='director',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DirectorM', to='FilmRevolutionApp.Movie'),
        ),
        migrations.AddField(
            model_name='director',
            name='serie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='DirectorS', to='FilmRevolutionApp.Serie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='platform',
            name='serie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FilmRevolutionApp.Serie'),
        ),
        migrations.AddField(
            model_name='production',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FilmRevolutionApp.Movie'),
        ),
        migrations.AddField(
            model_name='serie',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='serie',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
