# get data for all NASDAQ 100 stocks
# source for sticker list: https://cseweb.ucsd.edu/~yaq007/NASDAQ100_stock_data.html

import requests
import pandas as pd
from datetime import datetime, timedelta

api_key = 'cd8bc2e0d9aa1366cb71d12be8595628751cc215'
headers = {
    'Content-Type': 'application/json'
}

START_DATE = '2014-1-1'
END_DATE = '2024-1-1'

handle = open('../data/nasdaq_100.txt', 'r')
symbols = handle.readlines()[:-1]

for ticker in symbols:
    ticker = ticker.strip()
    print(ticker)
    ticker = 'NDX'

    url = f"https://api.tiingo.com/tiingo/daily/{ticker}/" \
            + "prices?startDate={START_DATE}&endDate={END_DATE}&token={api_key}"

    request_resp = requests.get(url, headers=headers)
    json = request_resp.json()
    print(json)

    prices = []
    volumes = []

    for time_item in json:
        prices.append(time_item["open"])
        volumes.append(time_item["volume"])

    dataframe = pd.DataFrame([ prices, volumes ]).T
    dataframe.to_pickle(f'../data/nasdaq/{ticker}.pkl')

    print(dataframe)
