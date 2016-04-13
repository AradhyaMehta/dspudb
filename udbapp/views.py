from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .models import University

from auditlog.models import LogEntry


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

def app_auditlog(request):
    entries = LogEntry.objects.all()
    log_data = {
        "logentries": entries
    }
    return render(request, "auditlog.html", log_data)

def custom400(request):
    response = render_to_response('400.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def custom403(request):
    response = render_to_response('403.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def custom404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

def custom500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response
