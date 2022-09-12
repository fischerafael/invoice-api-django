from django.db import models

class Client(models.Model):
    name = models.TextField(max_length=255)
    address = models.TextField(max_length=255)
    city = models.TextField(max_length=100)
    country = models.TextField(max_length=100)

    def __str__(self):
        return self.name
