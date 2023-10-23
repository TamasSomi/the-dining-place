from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm


@login_required
def dashboard(request):
    form_context = {}
    bookings = Booking.objects.filter(user=request.user).order_by('date_time')

    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
        else:
            form_context = {
                'booking_form': form,
                'bookings': bookings,
            }

    else:
        booking_form = BookingForm(user=request.user)
        form_context = {
            'booking_form': booking_form,
            'bookings': bookings,
        }
    return render(request, 'dashboard.html', form_context)


def index(request):
    return render(request, 'index.html')


def booking_success(request):
    return render(request, 'booking_success.html')


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == 'POST':
        if 'confirm' in request.POST:
            booking.delete()
            return redirect('dashboard')
        elif 'cancel' in request.POST:
            return redirect('dashboard')

    return render(request, 'delete_booking.html', {'booking': booking})


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = BookingForm(instance=booking)

    return render(
        request, 'edit_booking.html', {'form': form, 'booking': booking}
        )