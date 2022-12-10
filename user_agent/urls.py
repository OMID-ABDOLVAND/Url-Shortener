from django.urls import path, include

# urlpatterns = [
#
#     # Djoser and JWT URL
#     path('',
#

from django.urls import include, path
from . import views

urlpatterns = [
    path('<str:code>', views.RedirectorsDetail.as_view()),
]
