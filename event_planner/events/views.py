from django.shortcuts import render
from .models import Event
from invitations.models import Invitations

def event_list(request):
    data_event = Event.objects.all()
    data_invitations = Invitations.objects.all()
    return render(request, "events/event_detail.html", {"data_event": data_event, "data_invitations": data_invitations})