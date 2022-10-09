from django.db import models

# Create your models here.
class OrderTable(models.Model):
    id = models.IntegerField()
    order_id = models.IntegerField(primary_key=True)
    cost_usd = models.IntegerField()
    cost_rub = models.IntegerField()
    delivery_date = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.order_id} || {self.cost_rub} || {self.cost_usd}'
    