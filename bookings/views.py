from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import BookingForm


@login_required
def dashboard(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('booking_success')

    else:
        
        booking_form = BookingForm()

        form_context = {
            'booking_form': booking_form,
        }
    return render(request, 'dashboard.html', form_context)


def index(request):
    return render(request, 'index.html')


def booking_success(request):
    return render(request, 'booking_success.html')