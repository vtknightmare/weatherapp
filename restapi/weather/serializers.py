# weather/serializers.py

from rest_framework import serializers
from .models import Weather

class WeatherSerializer(serializers.ModelSerializer):
    """Serializer to map the Weather instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Weather
        fields = ('last_measured', 'date_created', 'temperature', 'temperature_type', 'zipcode')
        read_only_fields = ('last_measured', 'date_created')
