from rest_framework import serializers
from .models import CryptoPrice


class CryptoPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoPrice
        fields = ('rowId',
                  'crypto_name',
                  'open',
                  'close',
                  'high',
                  'low',
                  'volume',
                  'time',
                  'timestamp')