from django.contrib import admin
from .models import CryptoPrice

models_list = [CryptoPrice]
admin.site.register(models_list)

