import pandas as pd   
import numpy as np   

# Class that assigns a "regime" label to each row of data
class RegimeDetector:

    def __init__(self, df: pd.DataFrame):
        
        self.df = df.copy()

    def detect_regime(self):
        """
        Main entry point:
        - adds helper columns (trend + volatility flags)
        - assigns a regime label per row
        - returns dataframe with a new 'regime' column
        """

        self.add_trend_signal()        # identify trend direction using MAs
        self.add_volatility_signal()  # identify high/low volatility
        self.assign_regime()          # combine signals into final regime

        return self.df

    # -------------------------------------------------------------
    # 1) TREND SIGNAL (based on moving averages computed earlier)
    # -------------------------------------------------------------
    def add_trend_signal(self):
        """
        Uses short MA vs long MA:
        - If short MA > long MA → uptrend (+1)
        - If short MA < long MA → downtrend (-1)
        - Else → no clear trend (0)
        """

        # np.where(condition, value_if_true, value_if_false)
        self.df["trend_signal"] = np.where(
            self.df["ma_short"] > self.df["ma_long"], 1,   # uptrend
            np.where(
                self.df["ma_short"] < self.df["ma_long"], -1,  # downtrend
                0  # equal → no clear trend
            )
        )

    # -------------------------------------------------------------
    # 2) VOLATILITY SIGNAL (based on rolling std of returns)
    # -------------------------------------------------------------
    def add_volatility_signal(self):
        """
        Classify volatility into high/low using a threshold.
        Threshold chosen as the median volatility (robust baseline).
        """

        # Compute a central threshold (median is less sensitive to outliers than mean)
        vol_threshold = self.df["volatility"].median()

        # If current volatility > threshold → high volatility (1), else low (0)
        self.df["vol_signal"] = np.where(
            self.df["volatility"] > vol_threshold, 1, 0
        )

    # -------------------------------------------------------------
    # 3) FINAL REGIME ASSIGNMENT
    # -------------------------------------------------------------
    def assign_regime(self):
        """
        Combine trend + volatility into human-readable regimes:

        Rules:
        - Uptrend + Low Vol → "TREND_UP"
        - Downtrend + Low Vol → "TREND_DOWN"
        - No trend + Low Vol → "RANGE"
        - Any + High Vol → "HIGH_VOL"

        Priority:
        - High volatility overrides others (risk-first view)
        """

        regimes = []  # collect regime label per row

        
        for _, row in self.df.iterrows():

            # If high volatility → mark as HIGH_VOL regardless of trend
            if row["vol_signal"] == 1:
                regimes.append("HIGH_VOL")

            else:
                # Low volatility → use trend signal
                if row["trend_signal"] == 1:
                    regimes.append("TREND_UP")

                elif row["trend_signal"] == -1:
                    regimes.append("TREND_DOWN")

                else:
                    regimes.append("RANGE")

        # attach result as a new column
        self.df["regime"] = regimes