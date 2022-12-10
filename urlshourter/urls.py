from django.urls import path, include
from urlshourter import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.MakeShortUrl, basename='make_short_url')

urlpatterns = [
    path('', include(router.urls)),
    path('redirect/<str:code>/', views.Redirect.as_view({'get': 'retrieve'})),
]
