from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.app_home),
    url(r'^create/$', views.app_create),
    url(r'^retrieve/$', views.app_retrieve),
    url(r'^update/$', views.app_update),
    url(r'^delete/$', views.app_delete),
    url(r'^auditlog/$', views.app_auditlog),
    url(r'^admin/', admin.site.urls),
]
