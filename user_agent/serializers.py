from django.core.paginator import Paginator
from rest_framework import serializers
from user_agent.models import UserAgentModel
from django_cassandra_engine.rest.serializers import DjangoCassandraModelSerializer

class UserAgentSerializer(DjangoCassandraModelSerializer):
    class Meta:
        model = UserAgentModel
        fields = ['browser', 'os', 'ip']
        read_only_fields = ['browser', 'os', 'ip']

