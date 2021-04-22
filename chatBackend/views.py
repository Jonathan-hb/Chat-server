from chatBackend.models import persons, groups, messages
from rest_framework import viewsets
from rest_framework import permissions
from chatBackend.serializers import personsSerializer, groupsSerializer, messagesSerializer

class personsViewSet(viewsets.ModelViewSet):
    queryset = persons.objects.all()
    serializer_class = personsSerializer
    permission_classes = [permissions.IsAuthenticated]

class groupsViewSet(viewsets.ModelViewSet):
    queryset = groups.objects.all()
    serializer_class = groupsSerializer
    permission_classes = [permissions.IsAuthenticated]

class messagesViewSet(viewsets.ModelViewSet):
    queryset = messages.objects.all()
    serializer_class = messagesSerializer
    permission_classes = [permissions.IsAuthenticated]