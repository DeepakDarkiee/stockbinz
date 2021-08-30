from django.shortcuts import render
from django.views.generic import CreateView, View

# Create your views here.
class DataView(View):
  def get(self, request, *args, **kwargs):
    return render(request,'home/index.html')