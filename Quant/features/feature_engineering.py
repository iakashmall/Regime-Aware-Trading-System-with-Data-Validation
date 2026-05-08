import pandas as pd  
import numpy as np    

# Class to create features (indicators) from clean OHLCV data
class FeatureEngineer:

    def __init__(self, df: pd.DataFrame):
        #copy of input data to avoid modifying original dataset
        self.df = df.copy()

    def generate_features(self):
        """
        Main function that calls all feature creation steps
        """

        self.add_returns()           # calculate price returns
        self.add_moving_averages()  # calculate trend indicators
        self.add_volatility()       # calculate risk (volatility)
        self.add_rsi()              # calculate momentum indicator

        # Removing rows with NaN values created due to rolling calculations
        self.df.dropna(inplace=True)

        return self.df              # return dataframe with new features

    def add_returns(self):
        """
        Calculate percentage change in price
        """

        # pct_change() computes (current - previous) / previous
        self.df["returns"] = self.df["close"].pct_change()

    def add_moving_averages(self):
        """
        Calculate short-term and long-term moving averages
        """

        # rolling(window=10) → take last 10 rows
        # mean() → calculate average
        self.df["ma_short"] = self.df["close"].rolling(window=10).mean()

        # longer window → smoother trend
        self.df["ma_long"] = self.df["close"].rolling(window=50).mean()

    def add_volatility(self):
        """
        Calculate volatility using standard deviation of returns
        """

        # std() → measures how much values vary from mean
        self.df["volatility"] = self.df["returns"].rolling(window=10).std()

    def add_rsi(self, period=14):
        """
        Calculate Relative Strength Index (RSI): 
        momentum oscillator that measures the speed 
        and change of price movements on a scale from 0 to 100
        """

        # diff() → difference between current and previous price
        delta = self.df["close"].diff()

        # where(condition, value_if_false)
        # keep positive values, replace others with 0
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()

        # keep negative values (as positive), replace others with 0
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

        # Relative Strength
        rs = gain / loss

        # RSI formula
        self.df["rsi"] = 100 - (100 / (1 + rs))