from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Booking, validate_datetime, validate_pax
from django.contrib.auth.models import User


class BookingModelTestCase(TestCase):
    def setUP(self):
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )

    def test_validate_datetime_in_past(self):
        past_datetime = timezone.now() - timezone.timedelta(hours=1)
        with self.assertRaises(ValidationError):
            validate_datetime(past_datetime)

    def test_validate_datetime_in_future(self):
        future_datetime = timezone.now() + timezone.timedelta(hours=1)
        try:
            validate_datetime(future_datetime)
        except ValidationError:
            self.fail("validate_datetime raised an unexpected ValidationError")

    def test_validate_pax_invalid_less_than_one(self):
        invalid_pax = 0
        with self.assertRaises(ValidationError):
            validate_pax(invalid_pax)

    def test_validate_pax_invalid_more_than_twenty(self):
        invalid_pax = 21
        with self.assertRaises(ValidationError):
            validate_pax(invalid_pax)