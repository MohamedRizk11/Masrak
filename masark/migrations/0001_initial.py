# Generated by Django 5.0.4 on 2024-04-29 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roads',
            fields=[
                ('fid', models.IntegerField(verbose_name='FID')),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('time', models.IntegerField(verbose_name='Time')),
                ('distance', models.FloatField(max_length=15, verbose_name='Distane')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('fid', models.IntegerField(verbose_name='Fid')),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='User_ID')),
                ('status', models.CharField(choices=[('Normal', 'Normal'), ('Disabled', 'Disabled')], max_length=10, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='FamousPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='station_place', to='masark.station')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField(verbose_name='Cost')),
                ('time', models.FloatField(verbose_name='Time')),
                ('from_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_station', to='masark.station')),
                ('to_station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_station', to='masark.station')),
            ],
        ),
    ]
