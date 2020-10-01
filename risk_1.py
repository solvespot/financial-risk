import numpy as np
import pandas as pd
import pandas_datareader as pdr
import datetime as dt

start_date = dt.datetime(2017, 9, 26)
end_date = dt.datetime(2020, 9, 26)
tickers = ['es=f', 'zb=f', 'gc=f', 'cl=f']
close_prices = pdr.DataReader(tickers, data_source='yahoo', start=start_date, end=end_date)['Close']
print(close_prices.head(10))

close_prices.dropna(inplace=True)
close_prices.sort_index(ascending=False, inplace=True)
returns = (close_prices / close_prices.shift(-1) -1).dropna()
print(returns.describe())


x=1

x = np.DataF
y = pd.DataFrame()