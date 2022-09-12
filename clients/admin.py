from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'country', 'city']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'country']
    list_per_page = 20

admin.site.register(Client, ClientAdmin)


