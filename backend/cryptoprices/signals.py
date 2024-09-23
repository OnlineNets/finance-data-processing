from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CryptoPrice  # Replace with your actual model
from .consumers import PresenceConsumer
import json
from pprint import pprint
from datetime import datetime


@receiver(post_save, sender=CryptoPrice)
def notify_clients(sender, instance, created, **kwargs):
    msg = "New record created" if created else "Record updated"
    # Notify all connected clients

    pprint(instance)
    for connection in PresenceConsumer.connections:
        pprint(msg)
        connection.send(
            text_data=json.dumps({
                "msg": msg,
                "data": instance_to_dict(instance)  # You may need to create this function to format your instance
            })
        )

def instance_to_dict(instance):
    # Convert your model instance to a dictionary
    return {
        "rowId": instance.rowId,
        "crypto_name": instance.crypto_name,
        "open": instance.open,
        "close": instance.close,
        "high": instance.high,
        "low": instance.low_price,
        "volume": instance.volume,
        "timestamp": instance.timestamp,
        #"time": datetime.utcnow(),
        # Add other fields as necessary
    }