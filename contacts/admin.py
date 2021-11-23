from django.contrib import admin

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'listing', 'contact_date')


admin.site.register(Contact, ContactAdmin)
