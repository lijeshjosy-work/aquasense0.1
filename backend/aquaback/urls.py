from django.urls import path
from . import views

urlpatterns = [
   path('recieve_water_data/', views.recieve_water_data, name='recieve_water_data'),
   path('get_water_data/', views.get_water_data, name='get_water_data'),
]
