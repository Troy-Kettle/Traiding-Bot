import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies import Strategy
from lumibot.traders import Trader

from datetime import datetime

# Define the Alpaca credentials
API_KEY = 'API_KEY'
API_SECRET = 'API_SECRET'
BASE_URL = 'https://BASE_URL-api.alpaca.markets'

ALPACA_CREDS = {
    'API_KEY': API_KEY,
    'API_SECRET': API_SECRET,
    'BASE_URL': BASE_URL,
    'PAPER': True
}

# Define the trading strategy
class MLTrader(Strategy):
    def initialize(self, symbol: str = "SPY", lookback_period: int = 14):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None
        self.lookback_period = lookback_period
        self.data = []
        self.portfolio_values = []

    def on_trading_iteration(self):
        # Fetch latest price data
        current_price = self.get_last_price(self.symbol)
        self.data.append(current_price)

        # Ensure we have enough data for the lookback period
        if len(self.data) > self.lookback_period:
            self.data.pop(0)

            # Calculate the moving average
            moving_average = np.mean(self.data)

            # Simple trading logic: Buy if price is below moving average, sell if above
            if current_price < moving_average and (self.last_trade is None or self.last_trade == "sell"):
                order = self.create_order(self.symbol, 10, "buy", order_type="market")
                self.submit_order(order)
                self.last_trade = "buy"
            elif current_price > moving_average and self.last_trade == "buy":
                order = self.create_order(self.symbol, 10, "sell", order_type="market")
                self.submit_order(order)
                self.last_trade = "sell"

            # Track the portfolio value
            self.portfolio_values.append(self.get_portfolio_value())

    def on_finish(self):
        # Plot the portfolio value over time
        plt.figure(figsize=(10, 6))
        plt.plot(self.portfolio_values, label='Portfolio Value')
        plt.title('Portfolio Value Over Time')
        plt.xlabel('Trading Iteration')
        plt.ylabel('Portfolio Value (USD)')
        plt.legend()
        plt.grid(True)
        plt.show()

# Set the backtest parameters
start_date = datetime(2023, 12, 1)
end_date = datetime(2023, 12, 31)

# Initialize the broker and strategy
broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker=broker, parameters={"symbol": "SPY", "lookback_period": 14})

# Run the backtest
strategy.backtest(YahooDataBacktesting, start_date, end_date, parameters={})

# If you want to execute the strategy live, you can uncomment the following lines:
# trader = Trader(broker=broker, strategy=strategy)
# trader.run()
