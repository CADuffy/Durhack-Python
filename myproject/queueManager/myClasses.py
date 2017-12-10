import self as self
from django.db import models

# Create your models here.
class main:
    self.companies = []

    def __init__(self):
        companies = []

    def add_company(self, name, category):
        companies.append(Company(name, category))

    def create_customer(self, phoneNumber):


class Company:
    self.name = ""
    self.category = ""
    self.queue = []

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def get_customer_position(self, customer):
        found = False
        position = 0
        while found == False:
            if Company.queue[position] == customer:
                found = True
        return position

    def increment_customer_positions(self):
        for x in range(0, len(Company.queue)):
            Company.queue[x].increment_position()

    def add_customer(self, customer, index):
        queue.append(customer)
        customer.set_position(index, len(queue))


class Customer:
    self.phoneNumber = ""
    self.positions = []
    self.queues = []

    def __init__(self):
        self.phoneNumber = phoneNumber

    def get_position(self, queue):
        queue.get_customer_position(self)

    def set_position(self, queue):
        queue.get_customer_position(self)

    def join_queue(self, company):
        company.add_customer(self, len(queues) - 1)
        queues.append(company)

    def increment_position(self):
        Customer.position -= 1

