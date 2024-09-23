from django.apps import AppConfig


class CryptoPricesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cryptoprices"

    def ready(self):
        import cryptoprices.signals 