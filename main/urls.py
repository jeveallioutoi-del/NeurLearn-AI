from django.urls import path
from . import views

urlpatterns = [
    # HTML pages
    path('', views.index, name='index'),
    
    # API endpoints
]