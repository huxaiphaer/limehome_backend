from rest_framework import serializers

from reservations.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    """ReservationSerializer class."""
    class Meta:
        model = Reservation
        fields = ('first_name', 'last_name', 'check_in', 'check_out',
                  'number_of_guests', 'billing_address', 'billing_country',
                  'postal_code', 'city', 'email', 'phone_number',)

    def create(self, validated_data):
        """Create a reservation."""
        return Reservation.objects.create(**validated_data)

