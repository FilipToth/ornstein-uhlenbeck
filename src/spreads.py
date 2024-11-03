import time
import yfinance
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from alpha_vantage.timeseries import TimeSeries

api_key = 'SL50M7EW9JJWEQXM'
ts = TimeSeries(key=api_key, output_format='pandas')

def get_data(ticker, interval, months, end_date):
    price_frames = []

    current = end_date
    for _ in range(months):
        data, _ = ts.get_intraday(symbol=ticker, interval=interval, outputsize='full', extended_hours=False, adjusted='false')
        price_frames.append(data)

        print('got price data...')

        current -= timedelta(days=30)
        time.sleep(12)

    if not price_frames:
        return None

    full = pd.concat(price_frames)
    full = full[~full.index.duplicated(keep='first')]
    full = full.sort_index()
    full = full[full.index.dayofweek < 5]
    full = full.dropna(subset=['4. close'])
    full = full[full['4. close'] != full['4. close'].shift()]

    return full


START = datetime(2024, 8, 15)
NUM_MONTHS = 1
INTERVAL = "1min"
END_DATE = datetime(2024, 10, 15)

# PEP, KO
# pep = get_data("PEP", INTERVAL, NUM_MONTHS, END_DATE)[['4. close']]
ko = get_data("KO", INTERVAL, NUM_MONTHS, END_DATE)[['4. close']]

for index, row in ko.iterrows():
    print(row)

# pep.to_pickle('../data/pep.pkl')
ko.to_pickle('../data/ko.pkl')

# spreads = pep - ko
# spreads.to_pickle('../data/spreads.pkl')

# print(spreads)

# sns.lineplot(data=spreads)
sns.lineplot(data=ko)
# sns.lineplot(data=pep)

plt.show()