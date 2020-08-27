from yahoo_fin import stock_info as si
from yahoo_fin import options, requests
import pandas as pd

dow_tickers = si.tickers_dow()
nasdaq_tickers = si.tickers_nasdaq()
spy_tickers = si.tickers_sp500()

# replace DOW with DWDP in ticker list

# scrape the options data for each Dow ticker
data = pd.read_csv('tickers.csv')
for ticker in dow_tickers:
    try:
        ticker_data = options.get_options_chain(ticker)
        ticker_df = pd.DataFrame(ticker_data["calls"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "call"
        data = pd.concat([data, ticker_df])
        ticker_df = pd.DataFrame(ticker_data["puts"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "put"
        data = pd.concat([data, ticker_df])
    except Exception:
        print(ticker + " failed")

for ticker in nasdaq_tickers:
    try:
        ticker_data = options.get_options_chain(ticker)
        print(1)
        ticker_df = pd.DataFrame(ticker_data["calls"])
        print(2)
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "call"
        data = pd.concat([data, ticker_df])
        ticker_df = pd.DataFrame(ticker_data["puts"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "put"
        data = pd.concat([data, ticker_df])
    except Exception:
        print(ticker + " failed")

for ticker in spy_tickers:
    try:
        ticker_data = options.get_options_chain(ticker)
        ticker_df = pd.DataFrame(ticker_data["calls"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "call"
        data = pd.concat([data, ticker_df])
        ticker_df = pd.DataFrame(ticker_data["puts"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "put"
        data = pd.concat([data, ticker_df])
    except Exception:
        print(ticker + " failed")


data.drop_duplicates(inplace=True)
data.to_csv('tickers.csv', index=False)

# db_out = pd.concat([db, matched_data])
#chain = options.get_options_chain("nflx")
#df = pd.DataFrame(chain["calls"])
#df['Ticker Id'] = "nflx"
#df['Option Type'] = "call"

#df.to_csv('tickers.csv', index=False)
# print(df)
