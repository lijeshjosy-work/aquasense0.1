from rest_framework.decorators import api_view
from rest_framework.response import Response    
from django.http import HttpResponse
from .models import WaterLevel


# Create your views here.

@api_view(['GET'])
def recieve_water_data():
    
    percentage = WaterLevel.GET.get('percentage')
