from abc import ABC, abstractmethod
import pandas as pd
# data ingestion class
class BaseDataSource(ABC):

    @abstractmethod
    def fetch_ohlcv(self, symbol: str, timeframe: str, limit: int) -> pd.DataFrame:
        pass
