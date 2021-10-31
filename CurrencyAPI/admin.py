from django.contrib import admin

from .models import *

class CurrencyAdmin(admin.ModelAdmin):
    model = Currency
    list_display = ('id', 'name', 'rate')
    list_display_links = ('id', 'name')

admin.site.register(Currency, CurrencyAdmin)