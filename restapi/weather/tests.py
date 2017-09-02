# weather/tests.py
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import Weather

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.weather = {'zipcode': '24073', 'temperature': '72.5', 'temperature_type': 'F'}
        self.response = self.client.post(
            reverse('measure'),
            self.weather,
            format="json")

    def test_api_can_create_a_weather_entry(self):
        """Test the api has weather measuring capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_weather(self):
        """Test the api can get a given weather."""
        weather = Weather.objects.get()
        response = self.client.get(
          reverse('check', kwargs={'pk': weather.id}),
          format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, weather.temperature)

    def test_api_can_update_weather(self):
        """Test the api can update a given weather."""
        weather = Weather.objects.get()
        res = self.client.put(
          reverse('check', kwargs={'pk': weather.id}),
          self.weather, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_weather(self):
        """Test the api can delete a weather."""
        weather = Weather.objects.get()
        response = self.client.delete(
          reverse('check', kwargs={'pk': weather.id}),
          format='json',
          follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
