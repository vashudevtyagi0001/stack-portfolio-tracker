import yfinance as yf
import pandas as pd

class Stock:
    def __init__(self, ticker, quantity):
        self.ticker = ticker
        self.quantity = quantity
        self.data = yf.download(ticker, period='1y')

    def get_current_price(self):
        return self.data.iloc[-1]['Close']

    def get_historical_data(self):
        return self.data

    def get_total_value(self):
        return self.get_current_price() * self.quantity

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def get_total_value(self):
        total_value = 0
        for stock in self.stocks:
            total_value += stock.get_total_value()
        return total_value

    def get_stock_values(self):
        stock_values = {}
        for stock in self.stocks:
            stock_values[stock.ticker] = stock.get_total_value()
        return stock_values

portfolio = Portfolio()
stock1 = Stock('AAPL', 100)
stock2 = Stock('GOOG', 50)
portfolio.add_stock(stock1)
portfolio.add_stock(stock2)

print(f'Total portfolio value: ${portfolio.get_total_value():.2f}')
print('Stock values:')
for ticker, value in portfolio.get_stock_values().items():
    print(f'{ticker}: ${value:.2f}')


print('Historical data for AAPL:')
print(stock1.get_historical_data())