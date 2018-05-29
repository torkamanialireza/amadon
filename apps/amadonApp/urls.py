from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^amadon$', views.index),
    url(r'^buy$', views.buy),
    url(r'^amadon/checkout/$', views.checkout),
    url(r'^back$', views.back),
    url(r'^reset$', views.reset),
]
