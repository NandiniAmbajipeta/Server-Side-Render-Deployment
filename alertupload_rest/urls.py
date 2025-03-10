#from django.conf.urls import url, include
from rest_framework import routers
from . import views
from rest_framework.authtoken import views as rest_framework_views
from django.urls import path,re_path,include

urlpatterns = [
    # Alert POST
    path('images/', views.post_alert, name='post_alert'),
    #url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    re_path(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]