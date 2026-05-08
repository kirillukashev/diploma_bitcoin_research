import requests
import pandas as pd
from datetime import datetime, timezone

BASE = "https://external-api.kalshi.com/trade-api/v2"

def ts(date):
    return int(pd.Timestamp(date, tz="UTC").timestamp())

def get_kalshi_candles(series_ticker, market_ticker, start="2023-01-01", end="2025-12-31"):
    url = f"{BASE}/series/{series_ticker}/markets/{market_ticker}/candlesticks"
    params = {
        "start_ts": ts(start),
        "end_ts": ts(end),
        "period_interval": 1440,  # daily
        "include_latest_before_start": True
    }

    r = requests.get(url, params=params)
    r.raise_for_status()

    data = r.json()["candlesticks"]

    df = pd.DataFrame([
        {
            "date": pd.to_datetime(x["end_period_ts"], unit="s"),
            "prob": float(x["price"]["close_dollars"]) if x.get("price") and x["price"].get("close_dollars") else None,
            "volume": float(x["volume_fp"]) if x.get("volume_fp") else None,
            "open_interest": float(x["open_interest_fp"]) if x.get("open_interest_fp") else None,
        }
        for x in data
    ])

    return df.sort_values("date")