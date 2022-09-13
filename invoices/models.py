from django.db import models

from clients.models import Client

class Currency(models.Model):   
    name = models.TextField(max_length=10)   

    def __str__(self):
        return self.name

class Invoice(models.Model):
    date = models.DateField(auto_now=True)
    total = models.IntegerField(null=False) 
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  

    # def __str__(self):
    #     return self.date

