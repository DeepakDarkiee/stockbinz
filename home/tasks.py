import random
from celery import Celery
from celery import shared_task
from home.utils import mail
from celery.schedules import crontab
app = Celery()

@shared_task(name="contact_mail")
def contact_mail(recipient):
    mail(recipient)
    
    
@app.task
def add():
    z = 5 + 2
    print(z)
    return True

