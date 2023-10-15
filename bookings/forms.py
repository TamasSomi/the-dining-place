from django import forms
from .models import Booking
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BookingForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['user'].queryset = User.objects.filter(pk=user.pk)
