# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
import csv
import requests
import pandas as pd

symbol = 'ko'
api_key = 'SL50M7EW9JJWEQXM'
CSV_URL = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={symbol}&interval=1min&slice=year1month2&apikey={api_key}'

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    df=pd.DataFrame(my_list)
    print(df)