from django.conf.urls import *

from . import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
]
