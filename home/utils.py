from django.http import HttpResponse  
from stockbinz import settings  
from django.core.mail import send_mail  
  
  
def mail(recipient):  
    subject = "Greetings"  
    msg     = "Congratulations for your success"  
    to      = recipient 
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    return res