from django.db import models

# Create your models here.


class CryptoPrice(models.Model):
    rowId = models.AutoField(primary_key=True)
    crypto_name = models.CharField(max_length=10)
    open_price = models.FloatField()
    close_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    volume = models.FloatField()
    time = models.DateTimeField()
