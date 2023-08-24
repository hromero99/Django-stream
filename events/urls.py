from django.contrib import admin
from django.urls import path,include
from .views import event_list_view
urlpatterns = [
    path("",event_list_view)
]
