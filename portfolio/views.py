from django.shortcuts import render

# Create your views here.
from .models import Project
    #create your views here
    
def home(request):
    projects =Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})