# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .serializers import WeatherSerializer
from .models import Weather

class MeasureView(generics.ListCreateAPIView):
    """This class defines the post behavior of our rest api."""
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def perform_measure(self, serializer):
        """Save the post data when creating a new measurement."""
        serializer.save()

class CheckView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
