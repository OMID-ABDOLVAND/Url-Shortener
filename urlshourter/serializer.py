from rest_framework import serializers
from urlshourter.models import UrlModel


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlModel
        fields = ['long_url', 'user', 'code']
        read_only_fields = ['user', ]
