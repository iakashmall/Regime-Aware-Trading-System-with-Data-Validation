import requests
import pandas as pd
from datetime import datetime
from data_ingestion.base_data_source import BaseDataSource

class BinanceDataSource(BaseDataSource):
    BASE_URL = "https://api.binance.com/api/v3/klines"

    def fetch_ohlcv(self, symbol: str, timeframe: str = "1m", limit: int = 500) -> pd.DataFrame:
        params = {
            "symbol": symbol,
            "interval": timeframe,
            "limit": limit
        }

        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        df = pd.DataFrame(data, columns=[
            "timestamp", "open", "high", "low", "close", "volume",
            "close_time", "qav", "num_trades",
            "taker_base_vol", "taker_quote_vol", "ignore"
        ])

        # Keep only required columns
        df = df[["timestamp", "open", "high", "low", "close", "volume"]]
        print(df)
        # Convert data types
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')
        df[["open", "high", "low", "close", "volume"]] = df[
            ["open", "high", "low", "close", "volume"]
        ].astype(float)

        return df