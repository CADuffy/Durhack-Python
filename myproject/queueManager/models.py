from django.db import models

# Create your models here.
class main(models.Model):
    companies = []


class PhoneNumber(models.Model):
    pos = models.IntegerField()
    number0 = models.CharField(max_length=30)

class Company(models.Model):
    queue = []

    def get_customer_position(self, customer):
        found = false
        position = 0
        while found == false:
            if queue[position] == customer:
                found = true
        return position

    def update_customer_positions(self):
        for x in range(0, len(queue)):
            queue[x].update_position


class Customer(models.Model):
    phoneNumber = ""
    position = 0
    queues = []

    def get_position(self, queue):
        queue.get_customer_position(self)

    def update_position(self):
        position += 1
