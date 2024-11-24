from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')  # Ensure this matches your template's name
