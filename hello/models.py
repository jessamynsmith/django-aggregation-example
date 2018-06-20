from django.db import models


class Invoice(models.Model):
    description = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return '{}'.format(self.description)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.CharField(max_length=120, unique=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.total_cost = self.unit_cost * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return '{} ({} x {} = {})'.format(self.description, self.unit_cost,
                                          self.quantity, self.total_cost)
