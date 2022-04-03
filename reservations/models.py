from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_countries.fields import CountryField


class Reservation(TimeStampedModel, models.Model):
    """
    Reservation class.
    """
    first_name = models.CharField(
        'First Name', max_length=150, null=False, blank=False)
    last_name = models.CharField(
        'Last Name', max_length=150, null=False, blank=False)
    check_in = models.DateField(
        'Name', max_length=150, null=False, blank=False)
    check_out = models.DateField(
        'Name', max_length=150, null=False, blank=False)
    number_of_guests = models.IntegerField(
        'Number of guests', default=1)
    billing_address = models.CharField(
        'Billing Address', max_length=150, null=False, blank=False)
    billing_country = CountryField()
    postal_code = models.IntegerField(
        'Postal code', default=1)
    city = models.CharField(
        'City', max_length=150, null=False, blank=False)
    email = models.EmailField('Email', db_index=False, unique=True)
    phone_number = models.CharField(
        'Phone Number', max_length=150, null=False, blank=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
