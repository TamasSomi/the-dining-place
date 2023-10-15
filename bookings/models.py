from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=13)
    date_time = models.DateTimeField()
    pax = models.IntegerField(
        validators=[MinValueValidator(1)]
    )
    comments = models.TextField(blank=True)
