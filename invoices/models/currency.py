from django.db import models

class Currency(models.Model):   
    name = models.TextField(max_length=10)   

    def __str__(self):
        return self.name