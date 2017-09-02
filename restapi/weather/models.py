# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Weather(models.Model):
    temperature = models.DecimalField(decimal_places=2, max_digits=20)
    temperature_type = models.CharField(max_length=1, blank=False)
    zipcode = models.CharField(max_length=5, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_measured = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation."""
        return "{}{}-{}".format(self.temperature, self.temperature_type, self.zipcode)
