from django.urls import path
from .views import CryptoPriceView
from . import consumers
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("cryptoprices/", CryptoPriceView.as_view()),
    path("cryptoprices/<int:pk>/", CryptoPriceView.as_view()),
    path("ws/crypto", consumers.PresenceConsumer.as_asgi()),
]
