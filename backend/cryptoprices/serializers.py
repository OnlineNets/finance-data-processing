from rest_framework import serializers
from .models import CryptoPrice


class CryptoPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoPrice
        fields = ('rowId',
                  'crypto_name',
                  'open_price',
                  'close_price',
                  'high_price',
                  'low_price',
                  'volume',
                  'time')