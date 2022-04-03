from django.urls import path

from . import views

urlpatterns = [
    path('reservation/', views.ReservationView.as_view(), name='reservation'),
    path('countries/', views.CountriesView.as_view(), name='countries'),
]
