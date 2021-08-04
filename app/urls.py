from django.urls import path     
from . import views
urlpatterns = [
    path('', views.ninja),
    path('process_money/<str:name>', views.money),
    path('reset/', views.reset),    	   	   
]