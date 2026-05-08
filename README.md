# Regime-Aware-Trading-System-with-Data-Validation
A modular, production-inspired quantitative trading framework that combines market regime detection, data validation, and adaptive strategy switching for robust algorithmic trading research.

The system is designed to simulate how institutional quant pipelines process financial market data before making trading decisions.

📌 Project Overview

Traditional retail trading systems apply a single strategy across all market conditions, often leading to poor robustness during volatile or regime-shifting environments.

This project addresses that issue by:

Validating raw OHLCV market data
Engineering statistical and technical features
Detecting market regimes dynamically
Switching strategies based on detected regimes
Generating trading signals adaptively

The architecture is intentionally modular to resemble real-world quantitative trading infrastructure.

🚀 Core Features
✅ Data Ingestion Layer
Binance API integration
Historical CSV support
Standardized OHLCV formatting
Extensible source architecture
✅ Data Validation Engine

Institution-grade preprocessing pipeline:

Missing value detection
Timestamp consistency checks
OHLC integrity validation
Outlier/spike detection using Z-score analysis
Data quality scoring
✅ Feature Engineering

Generates trading and statistical indicators:

Returns
Moving Averages
Rolling Volatility
RSI (Relative Strength Index)
✅ Regime Detection Layer

Dynamic market state classification using:

Trend detection via moving averages
Volatility regime analysis
Hidden Markov Models using hmmlearn (planned integration)

Current regimes include:

TREND_UP
TREND_DOWN
RANGE
HIGH_VOL
✅ Strategy Engine

Adaptive strategy switching based on market regime:

Regime	Strategy
TREND_UP	Momentum
TREND_DOWN	Short Momentum
RANGE	Mean Reversion (RSI)
HIGH_VOL	Risk Reduction / No Trade
🏗️ System Architecture
Data Source
    ↓
Data Ingestion
    ↓
Data Validation
    ↓
Feature Engineering
    ↓
Regime Detection
    ↓
Strategy Engine
    ↓
Signal Generation
    ↓
(Upcoming)
Backtesting & Performance Analytics
📂 Project Structure
QUANT/
│
├── data_ingestion/
│   ├── __init__.py
│   ├── base_data_source.py
│   ├── binance_source.py
│   ├── csv_source.py
│   └── data_factory.py
│
├── validation/
│   └── data_validator.py
│
├── features/
│   └── feature_engineering.py
│
├── regime/
│   └── regime_detector.py
│
├── strategies/
│   └── strategy_engine.py
│
├── main.py
│
└── README.md
🧠 Technologies Used
Python
Pandas
NumPy
Requests
hmmlearn (planned)
Matplotlib (planned)
Backtrader / VectorBT (planned)
📊 Planned Enhancements
🔹 Hidden Markov Model Integration

Using hmmlearn for probabilistic regime classification:

Bull/Bear states
Volatility clustering
Latent market state estimation
🔹 Backtesting Engine
Equity curve generation
Sharpe Ratio
Drawdown analysis
Trade statistics
🔹 Live Trading Simulation
Streaming market data
Real-time validation
Dynamic signal execution
🔹 Risk Management
Stop-loss / take-profit
Position sizing
Volatility-adjusted exposure
⚙️ Installation
Clone Repository
git clone <your-repo-url>
cd QUANT
Create Virtual Environment
python -m venv venv
Activate Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
Install Dependencies
pip install pandas numpy requests hmmlearn
▶️ Running the Project

Run from the project root directory:

python main.py
📈 Learning Goals of This Project

This project focuses on understanding:

Financial time-series preprocessing
Quantitative feature engineering
Regime-aware trading systems
Statistical market modeling
Modular trading architecture
Production-style Python project structure
⚠️ Disclaimer

This project is intended for:

Educational purposes
Quantitative research
Portfolio demonstration

It is not financial advice and should not be used directly for live capital deployment without extensive testing.

👨‍💻 Author

Akash Mall
Electrical Engineering Student
Aspiring Quant Developer / Data-Driven Systems Engineer
