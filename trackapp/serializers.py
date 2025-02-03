from rest_framework import serializers
from .models import tracker

class trackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tracker
        fields = '__all__'