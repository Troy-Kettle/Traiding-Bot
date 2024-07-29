# MLTrader: A Moving Average Trading Strategy

## Overview

**MLTrader** is a trading strategy implemented using the `lumibot` library and Alpaca's API. This strategy uses a simple moving average to make buy and sell decisions on the SPY ETF. The strategy is backtested over a specified date range, and the portfolio value is tracked and plotted over time.

## Features

- **Moving Average Strategy**: The strategy buys when the price is below the moving average and sells when the price is above.
- **Data Management**: Maintains a rolling window of price data for moving average calculations.
- **Portfolio Tracking**: Tracks and plots the portfolio value over time.
- **Customizable Parameters**: Allows customization of the trading symbol and lookback period for the moving average.

## Requirements

- Python 3.x
- `numpy`
- `pandas`
- `matplotlib`
- `lumibot`
- Alpaca API credentials

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mltrader.git
   cd mltrader
   ```

2. Create a virtual environment and install the required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up your Alpaca API credentials in the script.

## Usage

### Backtesting

1. Open `ml_trader.py` and ensure your Alpaca API credentials are set correctly:
   ```python
   API_KEY = 'Your_Alpaca_API_Key'
   API_SECRET = 'Your_Alpaca_API_Secret'
   ```

2. Run the backtest:
   ```bash
   python ml_trader.py
   ```

3. The script will run the backtest and display a plot of the portfolio value over time.

### Live Trading

1. To run the strategy live, uncomment the following lines in `ml_trader.py`:
   ```python
   # trader = Trader(broker=broker, strategy=strategy)
   # trader.run()
   ```

2. Run the script:
   ```bash
   python ml_trader.py
   ```

## Strategy Details

### Initialization

The strategy initializes with the following parameters:
- `symbol`: The trading symbol (default is "SPY").
- `lookback_period`: The period for calculating the moving average (default is 14 days).

### Trading Logic

- **Buy Signal**: If the current price is below the moving average and no position is held or the last action was a sell.
- **Sell Signal**: If the current price is above the moving average and the last action was a buy.

### Portfolio Tracking

The strategy tracks the portfolio value at each trading iteration and plots it at the end of the backtest.

## Example Plot

An example plot of the portfolio value over time will be generated and displayed at the end of the backtest.

![Portfolio Value](portfolio_value.png)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any questions or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).
