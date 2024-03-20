# api/serializers.py

from rest_framework import serializers
from .models import Hoodies

class HoodiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoodies
        fields = '__all__'
