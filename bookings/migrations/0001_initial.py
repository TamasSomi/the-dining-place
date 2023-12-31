# Generated by Django 4.2.5 on 2023-10-23 10:13

import bookings.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=40)),
                ('phone_number', models.CharField(max_length=13)),
                ('date_time', models.DateTimeField(validators=[bookings.models.validate_datetime])),
                ('pax', models.PositiveIntegerField(default=1, validators=[bookings.models.validate_pax])),
                ('comments', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
