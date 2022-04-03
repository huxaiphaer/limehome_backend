from rest_framework import generics
from rest_framework import response, status

from django_countries import countries

from core import custom_classes
from reservations import serializers
from reservations.models import Reservation


class ReservationView(generics.ListCreateAPIView):
    """ReservationView class."""
    queryset = Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer
    pagination_class = custom_classes.StandardResponsePagination

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED, )
        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)


class CountriesView(generics.ListAPIView):
    """CountriesView class."""
    queryset = Reservation.objects.all()

    def get(self, request, *args, **kwargs):
        """Get countries."""
        list_of_countries = []
        for country in list(countries):
            list_of_countries.append(dict(code=country[0], country=country[1]))
        return response.Response(list_of_countries,
                                 status=status.HTTP_200_OK, )

