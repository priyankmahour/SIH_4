# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-03 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('B_ID', models.AutoField(primary_key=True, serialize=False)),
                ('des_latitude', models.FloatField(blank=True)),
                ('des_longitude', models.FloatField(blank=True)),
                ('booking_time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver_details',
            fields=[
                ('D_ID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=30)),
                ('password', models.CharField(blank=True, max_length=40)),
                ('mobile_no', models.CharField(blank=True, max_length=10)),
                ('vehicle_no', models.CharField(blank=True, max_length=10)),
                ('availability', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Driver_location_details',
            fields=[
                ('DLOC_ID', models.AutoField(primary_key=True, serialize=False)),
                ('u_lattitude', models.FloatField(blank=True)),
                ('u_longitude', models.FloatField(blank=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('D_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver_desc', to='testapp.Driver_details')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_details',
            fields=[
                ('H_ID', models.AutoField(primary_key=True, serialize=False)),
                ('h_name', models.CharField(blank=True, max_length=128)),
                ('type', models.CharField(blank=True, max_length=1)),
                ('h_latitude', models.FloatField(blank=True)),
                ('h_longitude', models.FloatField(blank=True)),
                ('distance', models.CharField(blank=True, max_length=128)),
                ('duration', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('U_ID', models.AutoField(primary_key=True, serialize=False)),
                ('mobile_no', models.CharField(blank=True, max_length=10)),
                ('f_name', models.CharField(blank=True, max_length=12)),
                ('l_name', models.CharField(blank=True, max_length=12)),
                ('email', models.EmailField(blank=True, max_length=40)),
                ('token', models.CharField(blank=True, max_length=1000)),
                ('user_status', models.BooleanField(default=True)),
                ('blood_type', models.CharField(blank=True, max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_location_details',
            fields=[
                ('LOC_ID', models.AutoField(primary_key=True, serialize=False)),
                ('u_lattitude', models.FloatField(blank=True)),
                ('u_longitude', models.FloatField(blank=True)),
                ('update_time', models.DateTimeField(auto_now_add=True)),
                ('U_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loc_desc', to='testapp.User_details')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='D_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='d_bookings', to='testapp.Driver_details'),
        ),
        migrations.AddField(
            model_name='booking',
            name='U_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_bookings', to='testapp.User_details'),
        ),
    ]