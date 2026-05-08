from data_ingestion.data_factory import get_data_source
from validation.data_validator import DataValidator
from features.feature_engineering import FeatureEngineer
from regime.regime_detector import RegimeDetector

# Fetch data
source = get_data_source("binance")
df = source.fetch_ohlcv("BTCUSDT", "1m", 300)

# Validate
validator = DataValidator(df)
clean_df, issues = validator.validate()

# Features
fe = FeatureEngineer(clean_df)
feature_df = fe.generate_features()

# Regime Detection
rd = RegimeDetector(feature_df)
regime_df = rd.detect_regime()
print (df)
#for index, row in regime_df.iterrows():
 #   print(row["timestamp"], row["close"], row["regime"])
print(regime_df[["timestamp", "close", "regime"]].to_string())

print(regime_df["regime"].value_counts())