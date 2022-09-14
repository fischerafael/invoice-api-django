from sqlite3 import Date
from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=64)
    dayRate = models.FloatField(default=0)

    def __str__(self) -> str:
        return str(self.title)