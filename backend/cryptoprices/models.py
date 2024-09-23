from django.db import models

# Create your models here.


class CryptoPrice(models.Model):
    rowId = models.AutoField(primary_key=True)
    crypto_name = models.CharField(max_length=10)
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.FloatField()
    time = models.DateTimeField()
    timestamp = models.BigIntegerField()

