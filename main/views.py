from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    # This view renders the index.html template, which is the main page of the application.
    return render(request, 'index.html')