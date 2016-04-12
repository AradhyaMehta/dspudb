from django.http import HttpResponse
from django.shortcuts import render

from .models import University

# Create your views here.

def app_home(request):
    universities = University.objects.all()
    univ_data = {
        "universities": universities
    }
    return render(request, "home.html", univ_data)

def app_create(request):
    return HttpResponse("<h1>Create</h1>")

def app_retrieve(request):
    return HttpResponse("<h1>Retrieve</h1>")

def app_update(request):
    return HttpResponse("<h1>Update</h1>")

def app_delete(request):
    return HttpResponse("<h1>Delete</h1>")
