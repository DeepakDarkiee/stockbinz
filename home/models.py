from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    subject = models.CharField(max_length=100)
    massage = models.TextField(blank=False)

    def __str__(self):
        return self.name
