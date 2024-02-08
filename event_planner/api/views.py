from rest_framework.response import Response
from rest_framework.decorators import api_view
from events.models import Event
from .serializers import EventSerializer

# Seznam událostí
@api_view(["GET"])
def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

# Detail události
@api_view(["GET"])
def event_detail(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

# Vytvoření události
@api_view(["POST"])
def event_create(request):
    serializer = EventSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Aktualizace události
@api_view(["POST"])
def event_update(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(instance=event, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# Smazání události
@api_view(["DELETE"])
def event_delete(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    
    return Response("Item deleted")