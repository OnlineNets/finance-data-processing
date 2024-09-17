from django.urls import path
from .views import CryptoPriceView

urlpatterns = [
    path("cryptoprices/", CryptoPriceView.as_view()),
    path("cryptoprices/<int:pk>/", CryptoPriceView.as_view())
]
