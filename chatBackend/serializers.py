from chatBackend.models import persons, groups, messages
from rest_framework import serializers


class personsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = persons
        fields = ['full_name', 'email', 'birthdate', 'description', 'profile_picture', 'nickname', 'created_at', 'updated_at']

class groupsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = groups
        fields = ['person', 'group_name', 'created_at', 'updated_at']

class messagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = messages
        fields = ['message', 'viewed', 'messageFrom', 'messageTo', 'created_at', 'updated_at']