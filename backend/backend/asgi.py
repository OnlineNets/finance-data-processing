import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter # <- Add this
from channels.auth import AuthMiddlewareStack # <- Add this
from cryptoprices.consumers import PresenceConsumer # <- Add this

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_websockets.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            PresenceConsumer.as_asgi()
        ),
    }
)