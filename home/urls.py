
from django.urls import path
from .views import *

urlpatterns = [
    path('',DataView.as_view(),name='datview'),
]