from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_datetime(value):
    if value < timezone.now():
        raise ValidationError("You can not book a table in the past.")


def validate_pax(value):
    if value < 1 or value > 20:
        raise ValidationError("You can not book a table for less than 1 person or more than 20 people")


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=13)
    date_time = models.DateTimeField(validators=[validate_datetime])
    pax = models.PositiveIntegerField(default=1, validators=[validate_pax])
    comments = models.TextField(blank=True)
