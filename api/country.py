from rest_framework import serializers
from django_countries.fields import Country



class CountryField(serializers.Field):
    def to_representation(self, value):
        if isinstance(value, Country):
            return value.name
        return None