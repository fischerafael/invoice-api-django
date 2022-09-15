from django.contrib import admin

from invoices.models.invoiceServices import InvoiceService
from .models.service import Service
from .models.invoice import Invoice, Currency


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'currency', 'total', 'client']
    list_display_links = ['id', 'client']
    search_fields = ['id', 'total']
    list_per_page = 20

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']
    list_per_page = 20

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'dayRate']
    list_display_links = ['title']
    search_fields = ['title']
    list_per_page = 20

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(InvoiceService)
