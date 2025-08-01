from twelvedata import TDClient
import os

# Put your TwelveData API key here if you're not using environment variables
TD_API_KEY = os.getenv("TD_API_KEY", "806dd29a09244737ae6cd1a305061557)

def get_live_candles(symbol="EUR/USD", interval="1min", outputsize=5):
    td = TDClient(apikey=TD_API_KEY)

    ts = td.time_series(
        symbol=symbol,
        interval=interval,
        outputsize=outputsize,
        timezone="UTC"
    )

    candles = ts.as_json()

    formatted = []
    for c in candles:
        formatted.append({
            "time": c["datetime"],
            "open": float(c["open"]),
            "high": float(c["high"]),
            "low": float(c["low"]),
            "close": float(c["close"])
        })

    return formatted[::-1]
