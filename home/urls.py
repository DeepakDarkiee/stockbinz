
from django.urls import path
from .views import *

urlpatterns = [
    path('contact/',ContactView.as_view(),name='contactview'),
    path('',HomeView.as_view(),name='home'),
]