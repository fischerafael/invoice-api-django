from django.db import models

from clients.models import Client
from invoices.models.currency import Currency
from invoices.models.paymentTerms import PaymentTerms

class Invoice(models.Model):
    date = models.DateField(auto_now=True)
    total = models.IntegerField(null=False) 
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  
    payment_terms = models.ForeignKey(PaymentTerms, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

