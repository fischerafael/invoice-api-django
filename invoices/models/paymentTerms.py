from django.db import models

class PaymentTerms(models.Model):   
    name = models.CharField(max_length=10, default='EOB')

    def __str__(self):
        return self.name