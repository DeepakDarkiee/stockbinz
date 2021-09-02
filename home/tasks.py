import random
from celery import shared_task
from home.utils import mail

@shared_task(name="contact_mail")
def contact_mail(recipient):
    mail(recipient)