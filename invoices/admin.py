from django.contrib import admin
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

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Currency, CurrencyAdmin)
