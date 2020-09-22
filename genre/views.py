from django.shortcuts import render
from .models import Mpttapp
# Create your views here.

def index(request):
    return render(request, 'index.html', {'Mpttapp': Mpttapp.objects.all()})
