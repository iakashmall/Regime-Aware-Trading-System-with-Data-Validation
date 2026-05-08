import pandas as pd
from .base_data_source import BaseDataSource


class CSVDataSource(BaseDataSource):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def fetch_ohlcv(self, symbol=None, timeframe=None, limit=None) -> pd.DataFrame:
        df = pd.read_csv(self.file_path)

        # Standardize column names
        df.columns = [col.lower() for col in df.columns]

        # Ensure required columns exist
        required_cols = ["timestamp", "open", "high", "low", "close", "volume"]
        df = df[required_cols]

        # Convert timestamp
        df["timestamp"] = pd.to_datetime(df["timestamp"])

        return df