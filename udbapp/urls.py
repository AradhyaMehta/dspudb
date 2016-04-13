from django.conf.urls import url
from django.contrib import admin

from . import views

from django.conf.urls import (handler400, handler403, handler404, handler500)

handler400 = views.custom400
handler403 = views.custom403
handler404 = views.custom404
handler500 = views.custom500

urlpatterns = [
    url(r'^$', views.app_home),
    url(r'^create/$', views.app_create),
    url(r'^retrieve/$', views.app_retrieve),
    url(r'^update/$', views.app_update),
    url(r'^delete/$', views.app_delete),
    url(r'^auditlog/$', views.app_auditlog),
    url(r'^admin/', admin.site.urls),
]
