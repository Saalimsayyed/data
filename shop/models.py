from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user_name = models.CharField(max_length=100)
    feet = models.PositiveSmallIntegerField(default=0)
    given = models.PositiveIntegerField()
    back = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    duration_unit = models.CharField(max_length=10, choices=[('day', 'Day'), ('month', 'Month')])

    @property
    def total_price(self):
        if self.duration_unit == 'month':
            return self.price * self.quantity * self.duration * 30  # Assuming 30 days in a month
        return self.price * self.quantity * self.duration

    def __str__(self):
        return self.name
