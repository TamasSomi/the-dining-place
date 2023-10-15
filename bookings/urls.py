from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]