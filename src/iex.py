api_key = 'cd8bc2e0d9aa1366cb71d12be8595628751cc215'

import requests

headers = {
    'Content-Type': 'application/json'
}

requestResponse = requests.get("https://api.tiingo.com/iex/aapl/prices?startDate=2019-01-02&resampleFreq=5min&columns=open,high,low,close,volume&token=cd8bc2e0d9aa1366cb71d12be8595628751cc215", headers=headers)
print(requestResponse.json())
