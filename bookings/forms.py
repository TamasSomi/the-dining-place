from django import forms
from .models import Booking
from django.contrib.auth.models import User


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    # Show only the authorised user as options.
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BookingForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['user'].initial = user 
            self.fields['user'].queryset = User.objects.filter(pk=user.pk)

    # Check if booking already exists
    def clean(self):
        cleaned_data = super().clean()
        date_time = cleaned_data.get('date_time')
        user = cleaned_data.get('user')

        if date_time and user:
            existing_reservation = Booking.objects.filter(
                user=user,
                date_time=date_time
            )

            if self.instance and self.instance.pk:
                existing_reservation = existing_reservation.exclude(
                    pk=self.instance.pk
                )

            if existing_reservation.exists():
                raise forms.ValidationError(
                    "You already have a reservation for this time."
                )
