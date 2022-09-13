from django.db import models

from clients.models import Client
from invoices.models.currency import Currency

PAYMENT_TERMS = [(1, 'EOB'), (2, 'EOM')]

class Invoice(models.Model):
    date = models.DateField(auto_now=True)
    total = models.IntegerField(null=False) 
    paymentTerms = models.CharField(max_length=20,choices=PAYMENT_TERMS, default='EOB')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  
    client = models.ForeignKey(Client, on_delete=models.CASCADE)     

    def __str__(self):
        return str(self.date)

