from django.db import models

class PhoneNumber(models.Model):
    pos = models.IntegerField(default=0)
    numbers0 = models.CharField(max_length=30)
    class Meta:
        db_table = 'queues'
