import requests
import pandas as pd
from datetime import datetime, timedelta

api_key = 'cd8bc2e0d9aa1366cb71d12be8595628751cc215'
headers = {
    'Content-Type': 'application/json'
}

TICKER = 'pep'
START_DATE = datetime(2024, 9, 1)
NUM_DAYS = 30
SAMPLE_FREQ = '1min'

prices = []
volumes = []

current = START_DATE
for i in range(NUM_DAYS):
    date_str = current.strftime("%Y-%m-%d")
    current += timedelta(days=1)

    print(date_str)

    requestResponse = requests.get(f"https://api.tiingo.com/iex/{TICKER}/prices?startDate={date_str}&endDate={date_str}&resampleFreq={SAMPLE_FREQ}&columns=open,volume&token={api_key}", headers=headers)
    json = requestResponse.json()

    for time_item in json:
        prices.append(time_item["open"])
        volumes.append(time_item["volume"])

dataframe = pd.DataFrame([ prices, volumes ]).T
dataframe.to_pickle(f'../data/{TICKER}.pkl')

print(dataframe)
