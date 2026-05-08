import pandas as pd   # pandas → used for handling tabular data (like Excel sheets)
import numpy as np    # numpy → used for numerical operations (math, arrays)

# Define a class (blueprint) for validating market data
class DataValidator:

    def __init__(self, df: pd.DataFrame):
        # __init__ runs automatically when object is created

        self.df = df.copy()  
        # copy() → prevents modifying original data (important safety practice)

        self.issues = []  
        # list to store problems found in data

    def validate(self):
        """
        Running all validation checks
        """

        self.check_missing_values()       # check for missing data
        self.check_timestamp_order()      # check if time is sorted
        self.check_ohlc_consistency()     # check financial correctness
        self.detect_outliers()            # detect abnormal price movements

        return self.df, self.issues       # return cleaned data + issues list
    
    def check_missing_values(self):

        # isnull() → finds missing values (NaN)
        # .values.any() → checks if ANY missing value exists
        if self.df.isnull().values.any():

            self.issues.append("Missing values detected")  
            # log the issue
             
            # fillna(method='ffill') → forward fill
            # replaces missing value with previous valid value
            self.df.fillna(method='ffill', inplace=True)

    def check_timestamp_order(self):

        # is_monotonic_increasing → checks if timestamps are sorted
        if not self.df["timestamp"].is_monotonic_increasing:

            self.issues.append("Timestamps not in order")

            # sort_values → sorts data by time
            self.df = self.df.sort_values("timestamp")

    def check_ohlc_consistency(self):

        # condition checks invalid financial data
        condition = (
            (self.df["high"] < self.df["low"]) |     # high must be ≥ low
            (self.df["open"] > self.df["high"]) |    # open must be ≤ high
            (self.df["open"] < self.df["low"]) |     # open must be ≥ low
            (self.df["close"] > self.df["high"]) |   # close must be ≤ high
            (self.df["close"] < self.df["low"])      # close must be ≥ low
        )

        # condition.any() → checks if any row violates rules
        if condition.any():

            self.issues.append("OHLC inconsistency detected")

            # ~condition → keeps only valid rows
            self.df = self.df[~condition]

    def detect_outliers(self, z_thresh=3):

        # pct_change() → calculates percentage return between prices
        returns = self.df["close"].pct_change()

        # z-score formula:
        # (value - mean) / std deviation
        z_scores = (returns - returns.mean()) / returns.std() #How far a value is from normal behavior

        # np.abs() → absolute value (ignore sign)
        # > z_thresh → detect extreme values
        outliers = np.abs(z_scores) > z_thresh

        # check if any outliers exist
        if outliers.any():

            self.issues.append("Outliers detected in price")

            # mark outliers as NaN (remove bad data)
            self.df.loc[outliers, "close"] = np.nan

            # fill missing values using forward fill
            self.df["close"].fillna(method='ffill', inplace=True)

    def get_quality_score(self):

        # start with perfect score (100)
        score = 100 - (len(self.issues) * 10)

        # ensure score is not negative
        return max(score, 0)