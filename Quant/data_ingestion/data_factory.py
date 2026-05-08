from data_ingestion.binance_source import BinanceDataSource
from data_ingestion.csv_source import CSVDataSource

def get_data_source(source_type: str, **kwargs):
    if source_type == "binance":
        return BinanceDataSource()
    elif source_type == "csv":
        return CSVDataSource(kwargs.get("file_path"))
    else:
        raise ValueError("Unsupported data source")