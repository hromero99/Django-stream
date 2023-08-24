from rest_framework.views import APIView
from rest_framework.response import Response
from events.models import Event
from events.serializers.event_serializer import EventSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated


class EventListView(APIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]    
    def get(self,request,format=None):
        events = Event.objects.all()
        event_serializer = EventSerializer(events,many=True)
        
        return Response(
                data=event_serializer.data,
                status = 200
            )
    
    def post(self,request,format=None):
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(data=event_serializer.data,status=status.HTTP_200_OK)
        return Response(data={"error": event_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        