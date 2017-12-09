from django.db import models

class PhoneNumber(models.Model):
    pos = models.IntegerField(default=0)
    number0 = models.CharField(max_length=30)

