from django.shortcuts import render
from django.http import request
from .models import Event

def event_list_view(request):
    events = Event.objects.all()
    return render(request=request,template_name="event_list.html",context={"events": events})
