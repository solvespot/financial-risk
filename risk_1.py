import numpy as np
import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sbs

end_date = dt.datetime.today()
start_date = end_date - dt.timedelta(weeks=156)
tickers = ['es=f', 'ym=f', 'nq=f', 'zb=f', 'zf=f', 'gc=f', 'si=f', 'cl=f', 'ng=f']
names = ['S&P', 'Dow', 'Nasdaq', 'US T 10y', 'US T 5Y', 'Gold', 'Silver', 'Crude', 'Nat Gas']
mapping = {t: n for t, n in zip(tickers, names)}
close_prices = pdr.DataReader(tickers, data_source='yahoo', start=start_date, end=end_date)['Close']
close_prices.rename(columns=mapping, inplace=True)
print(close_prices[['Nasdaq', 'US T 10y']].head(5))

close_prices.dropna(inplace=True)
close_prices.sort_index(ascending=False, inplace=True)
returns = (close_prices / close_prices.shift(-1) - 1).dropna()
print(returns.describe())

sbs.heatmap(returns.corr(), cmap='RdYlGn', annot=True)
plt.show()

a = np.ndarray()
p = pd.DataFrame()
