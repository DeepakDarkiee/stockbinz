import requests
from django.http import HttpResponse  
from stockbinz import settings  
from django.core.mail import send_mail  
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def mail(recipient):  
    subject = "Greetings"   
    html_message = render_to_string('email/mail_template.html', {'context': 'values'})
    plain_message = strip_tags(html_message)
    to      = recipient 
    res     = send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [to],html_message=html_message)
    return res




_QUOTE_URL = "https://quotes.rest/qod"


def get_day_quote():
    """Get a day quote."""

    res = requests.get(_QUOTE_URL)
    return res.json()["contents"]["quotes"][0]["quote"]


def display_quote():
    """Display a random quote."""

    print(f'Quote Of The Day: "{get_day_quote()}"')