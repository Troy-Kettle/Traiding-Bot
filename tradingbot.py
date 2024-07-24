from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies import Strategy
from lumibot.traders import Trader

from datetime import datetime

API_KEY = 'CK9F9QE7XZ9I69VXAJ41'
API_SECRET = 'UgUy7R48JmQAR8RDZb3zTVji1IbGb0KrqhEgDT0r'
BASE_URL = 'https://paper-api.alpaca.markets'

ALAPACA_CREDS = {
    'API_KEY': API_KEY,
    'API_SECRET': API_SECRET,
    'PAPER': True
}

class MLTrader(Strategy):
    def initialise(self, symbol:str="SPY"):
        self.symbol = symbol
        self.sleeptime = "24H"
        self.last_trade = None
    def on_trading_iteration(self):
        if self.last_trade == None:
            order = self.create_order(self.symbol, 10, "buy", type="market")
            self.submit_order(order)
            self.last_trade = "buy"


start_date = datetime(2023, 12, 1)
end_date = datetime(2023, 12, 31)

broker = Alpaca(ALAPACA_CREDS)
strategy = MLTrader(name='mlstrat', broker=broker,
                    parameters={"symbol": "SPY"})
strategy.backtest(YahooDataBacktesting,
                  start_date,
                  end_date,
                  paramters={})

