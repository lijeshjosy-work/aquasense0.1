from rest_framework import serializers
from models import WaterLevel

class WaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterLevel
        fields = '__all__'