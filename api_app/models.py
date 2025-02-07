from django.db import models

# Table A - Customers
class A(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

