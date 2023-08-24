from django.contrib import admin
from django.urls import path,include
from events.api_views.event_list import EventListView
urlpatterns = [
    path("",EventListView.as_view())
]
