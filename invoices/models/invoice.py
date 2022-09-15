from email.policy import default
from django.db import models

from clients.models import Client
from invoices.models.currency import Currency
from invoices.models.service import Service

PAYMENT_TERMS = (
       ('eob', ('end of business day')),
       ('eom', ('end of month')),
       
   )

class Invoice(models.Model):
    date = models.DateField(auto_now=True)
    total = models.IntegerField(null=False) 
    paymentTerms = models.CharField(max_length=62,choices=PAYMENT_TERMS, default='eom')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  
    client = models.ForeignKey(Client, on_delete=models.CASCADE)   
   
    def __str__(self):
        return str(self.date)

