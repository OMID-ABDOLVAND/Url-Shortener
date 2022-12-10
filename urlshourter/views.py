from django.shortcuts import redirect
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from urlshourter.models import UrlModel
from urlshourter.serializer import UrlSerializer
from user_agent.tasks import save_redirector_detail
# Create your views here.

class MakeShortUrl(ModelViewSet):
    serializer_class = UrlSerializer
    queryset = UrlModel.objects.all()
    
    def get_permissions(self):
        if self.action in ['destroy', 'list', 'update']:
             self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        serializer.save()


class Redirect(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = UrlModel.objects.all()
    lookup_field = 'code'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        main_url = instance.long_url
        code = instance.code
        save_redirector_detail(request=request, url=code)
        return redirect(main_url)
