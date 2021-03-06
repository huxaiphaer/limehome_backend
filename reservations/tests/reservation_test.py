import json
import pytest
from rest_framework.test import APIClient

from unittest import TestCase
from django.urls import reverse


@pytest.mark.django_db
class ReservationTests(TestCase):
    """Reservation Tests."""

    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "first_name": "Huzy",
            "last_name": "Idris",
            "check_in": "2022-4-4",
            "check_out": "2022-4-9",
            "number_of_guests": 2,
            "billing_address": "Huzaifah",
            "billing_country": "UG",
            "postal_code": 23455,
            "city": "Kampala",
            "email": "huxy@gmail.com",
            "phone_number": "0704594180"
        }

    def test_make_reservation(self):
        """Make a reservation test."""
        response = self.client.post(
            reverse("reservation"), data=json.dumps(self.user_data),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_reservations(self):
        """Get all reservations test."""
        response = self.client.get(
            reverse("reservation"),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_missing_any_required_field(self):
        """Make a reservation while missing a required field test."""
        self.user_data['email'] = ''
        response = self.client.post(
            reverse("reservation"), data=json.dumps(self.user_data),
            content_type='application/json')
        self.assertEqual(str(response.data['email'][0]),
                         "This field may not be blank.")

    def test_email_duplicates_while_reserving(self):
        """Make a reservation while using duplicate email test."""
        self.client.post(
            reverse("reservation"), data=json.dumps(self.user_data),
            content_type='application/json')
        response = self.client.post(
            reverse("reservation"), data=json.dumps(self.user_data),
            content_type='application/json')
        self.assertEqual(str(response.data['email'][0]),
                         "reservation with this Email already exists.")

    def test_list_of_countries(self):
        """Get list of all countries"""
        response = self.client.get(
            reverse("countries"),
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

