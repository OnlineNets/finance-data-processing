# Generated by Django 5.1.1 on 2024-09-24 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoPrice',
            fields=[
                ('rowId', models.AutoField(primary_key=True, serialize=False)),
                ('crypto_name', models.CharField(max_length=10)),
                ('open', models.FloatField()),
                ('close', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('volume', models.FloatField()),
                ('period', models.DateTimeField()),
                ('timestamp', models.BigIntegerField()),
                ('rsi', models.FloatField()),
                ('macd', models.FloatField()),
            ],
        ),
    ]
