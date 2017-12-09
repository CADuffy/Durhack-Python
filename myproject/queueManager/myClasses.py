import self as self
from django.db import models

# Create your models here.
class main():
    companies = []

class Company():
    queue = []
    def get_customer_position(self, customer):
        found = False
        position = 0
        while found == False:
            if Company.queue[position] == customer:
                found = True
        return position

    def update_customer_positions(self):
        for x in range(0, len(Company.queue)):
            Company.queue[x].update_position


class Customer():
    self.phoneNumber = ""
    self.position = 0
    self.queues = []

    def get_position(self, queue):
        queue.get_customer_position(self)

    def update_position(self):
        Customer.position += 1
