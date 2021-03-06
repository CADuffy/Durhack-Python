from django.db import models


class PhoneNumber(models.Model):
    pos = models.IntegerField(default=0, primary_key=True)
    numbers = models.CharField(max_length=30)

class companyRecord(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    company_name = models.CharField(max_length=30)
    company_password = models.CharField(max_length=30)
    company_type = models.CharField(max_length=30)
    class Meta:
        db_table = 'companies'
