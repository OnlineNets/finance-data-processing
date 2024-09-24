import os
import json, talib, numpy
import websocket as wb
from pprint import pprint
from datetime import datetime
from django.conf import settings
import django

# Set up Django settings and initialize Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from cryptoprices.models import CryptoPrice

BINANCE_SOCKET = "wss://stream.binance.com:9443/stream?streams=ethusdt@kline_1m"
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = "ETHUSD"
TRADE_SIZE = 0.05
closed_prices = []
in_position = False

def on_open(ws):
    print("Connection opened")

def on_close(ws, close_status_code, close_msg):
    print(f"Connection closed with status code: {close_status_code} and message: {close_msg}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_message(ws, message):
    message = json.loads(message)
    candle = message["data"]["k"]
    pprint(candle)
    symbol = candle["s"]
    is_candle_closed = candle["x"]

    if is_candle_closed:
        closed = float(candle["c"])
        open = float(candle["o"])
        high = float(candle["h"])
        low = float(candle["l"])
        volume = float(candle["v"])
        interval = candle["i"]
        timestamp = int(candle["t"])

        pprint(f"Closed: {closed}")
        pprint(f"Open: {open}")
        pprint(f"High: {high}")
        pprint(f"Low: {low}")
        pprint(f"Volume: {volume}")
        pprint(f"Interval: {interval}")
        pprint(f"Is candle closed: {timestamp}")

        # Save to Django model
        crypto = CryptoPrice(
            crypto_name=symbol,
            open=open,
            close=closed,
            high=high,
            low=low,
            volume=volume,
            timestamp=timestamp,
            period=datetime.fromtimestamp(timestamp),
        )
        crypto.save()

        closes.append(closed)
        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            pprint("all rsis calculated so far")
            last_rsi = rsi[-1]
            macd, signal, hist = talib.MACD(np_closes, fastperiod=12, slowperiod=26, signalperiod=9)
            last_macd = macd[-1]

# Create WebSocket app
ws = wb.WebSocketApp(BINANCE_SOCKET, on_open=on_open, on_close=on_close, on_error=on_error, on_message=on_message)
ws.run_forever()