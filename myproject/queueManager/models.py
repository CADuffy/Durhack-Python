from django.db import models

class PhoneNumber(models.Model):
    pos = models.IntegerField(default=0, primary_key=True)
    number = models.CharField(max_length=30)
    class Meta:
        db_table = 'queues'

class companyRecord(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    company_name = models.CharField(max_length=30)
    company_password = models.CharField(max_length=30)
    company_type = models.CharField(max_length=30)
    class Meta:
        db_table = 'companies'
