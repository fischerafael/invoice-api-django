from django.db import models

from clients.models import Client

class Invoice(models.Model):
    date = models.DateField(auto_now=True)
    currency = models.TextField(max_length=120)
    total = models.IntegerField(null=False) 
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  

    def __str__(self):
        return self.id
