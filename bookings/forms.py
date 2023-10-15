from django import forms
from .models import Booking
from django.core.validators import MinValueValidator


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }