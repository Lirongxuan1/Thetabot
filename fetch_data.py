import os
from yahoo_fin import options, requests
import pandas as pd
import pickle
from datetime import datetime
os.chdir("C:\\Users\\Liron\\Desktop\\Thetabot")
now = datetime.now()
date_time = now.strftime("%m-%d-%Y-%H")
tickers = pickle.load(open('list.pkl', 'rb'))
print(date_time)
for ticker in tickers:
    try:
        ticker_data = options.get_options_chain(ticker)
        ticker_df = pd.DataFrame(ticker_data["calls"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "call"
        ticker_df.to_csv(date_time+ '.csv', mode="a", header=False, index=False)
        ticker_df = pd.DataFrame(ticker_data["puts"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "put"
        ticker_df.to_csv(date_time + '.csv', mode="a", header=False, index=False)
    except Exception:
        print(ticker + " failed")
print('done')
