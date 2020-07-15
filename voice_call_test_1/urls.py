from django.contrib import admin
from django.conf.urls import url 
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("call",views.call),
    path("receiver",views.receiver),
    url(r'^api/voice_call_test_1/sender_number$',views.voice_call_post),
    url(r'^api/voice_call_test_1/put/(?P<sender_number>\d+)',views.voice_call_put),
    url(r'^api/voice_call_test_1/get/(?P<sender_number>\d+)',views.voice_call_get),
]
