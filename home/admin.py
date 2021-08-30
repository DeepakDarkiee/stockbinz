from django.contrib import admin
from home.models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','subject']
    
    
admin.site.register(Contact, ContactAdmin)