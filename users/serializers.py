from rest_framework import serializers
from .models import Offence,Rider

class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider 
        fields = '__all__'

class OffenceSerializer(serializers.ModelSerializer):
    vehicle=RiderSerializer()
    class Meta:
        model = Offence
        fields = '__all__'