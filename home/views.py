from django.core.mail import send_mail
from django.views.generic import CreateView, View
from django.shortcuts import render,redirect,HttpResponse
from home.utils import get_day_quote
from home.models import Quotation

from home.models import Contact
# Create your views here.
from home.tasks import contact_mail

class ContactView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        subject = request.POST["subject"]
        massage = request.POST["massage"]
        data = Contact(
            name=name, email=email, phone=phone, subject=subject, massage=massage
        )
        data.save()
        contact_mail.delay(email)
       
        return HttpResponse('OK')


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/index.html")
    
    
class QuotesView(View):
    def get(self, request, *args, **kwargs):
        quote = get_day_quote()
        Quotation.objects.create(quote=quote)
        return render(request, "home/index.html")
