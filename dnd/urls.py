from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.home, name='dnd-home'),  
    path('contacts/', views.contacts, name='dnd-contacts'),  
]