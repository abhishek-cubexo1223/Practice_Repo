from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]

    first_name = models.CharField(max_length=255)  # Customer First Name
    last_name = models.CharField(max_length=255)   # Customer Last Name
    email = models.EmailField(unique=True)        # Unique Email
    phone = models.CharField(max_length=30)       # Phone Number
    city = models.CharField(max_length=100)       # City Name
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total Order Amount
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')  # Order Status

    def __str__(self):
        return f"Order {self.id} - {self.first_name} {self.last_name} ({self.status})"
