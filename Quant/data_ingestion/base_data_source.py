from abc import ABC, abstractmethod
import pandas as pd

class BaseDataSource(ABC):

    @abstractmethod
    def fetch_ohlcv(self, symbol: str, timeframe: str, limit: int) -> pd.DataFrame:
        pass