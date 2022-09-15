from email.policy import default
from django.db import models
from invoices.models.invoice import Invoice
from invoices.models.service import Service

class InvoiceService(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='services')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='invoices')
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return str(self.id)

    
