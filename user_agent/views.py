# Create your views here.
from rest_framework import generics

from urlshourter.models import UrlModel
from user_agent.models import UserAgentModel
from user_agent.serializers import UserAgentSerializer


class RedirectorsDetail(generics.ListAPIView):
    serializer_class = UserAgentSerializer

    def get_queryset(self):
        queryset = UserAgentModel.objects.filter(url=self.kwargs['code'])
        return queryset



