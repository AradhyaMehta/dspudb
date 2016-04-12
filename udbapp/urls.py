from django.conf.urls import url
from django.contrib import admin

from .views import app_home, app_retrieve, app_create, app_update, app_delete

urlpatterns = [
    url(r'^$', app_home),
    url(r'^create/$', app_create),
    url(r'^retrieve$', app_retrieve),
    url(r'^update/$', app_update),
    url(r'^delete/$', app_delete),
    url(r'^admin/', admin.site.urls),
]
