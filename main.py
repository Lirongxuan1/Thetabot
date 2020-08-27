from yahoo_fin import stock_info as si
from yahoo_fin import options, requests
import pandas as pd

dow_tickers = si.tickers_dow()
nasdaq_tickers = si.tickers_nasdaq()
spy_tickers = si.tickers_sp500()

# replace DOW with DWDP in ticker list
dow_tickers.remove('DOW')

# scrape the options data for each Dow ticker
for ticker in dow_tickers:
    try:
        ticker_data = options.get_options_chain(ticker)
        ticker_df = pd.DataFrame(ticker_data["calls"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "call"
        ticker_df.to_csv("tickers.csv", mode="a", header=False, index=False)
        ticker_df = pd.DataFrame(ticker_data["puts"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "put"
        ticker_df.to_csv("tickers.csv", mode="a", header=False, index=False)
    except Exception:
        print(ticker + " failed")

for ticker in nasdaq_tickers:
    try:
        ticker_data = options.get_options_chain(ticker)
        ticker_df = pd.DataFrame(ticker_data["calls"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "call"
        ticker_df.to_csv("tickers.csv", mode="a", header=False, index=False)
        ticker_df = pd.DataFrame(ticker_data["puts"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "put"
        ticker_df.to_csv("tickers.csv", mode="a", header=False, index=False)
    except Exception:
        print(ticker + " failed")

for ticker in spy_tickers:
    try:
        ticker_data = options.get_options_chain(ticker)
        ticker_df = pd.DataFrame(ticker_data["calls"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "call"
        ticker_df.to_csv("tickers.csv", mode="a", header=False, index=False)
        ticker_df = pd.DataFrame(ticker_data["puts"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "put"
        ticker_df.to_csv("tickers.csv", mode="a", header=False, index=False)
    except Exception:
        print(ticker + " failed")


# db_out = pd.concat([db, matched_data])
#chain = options.get_options_chain("nflx")
#df = pd.DataFrame(chain["calls"])
#df['Ticker Id'] = "nflx"
#df['Option Type'] = "call"

#df.to_csv('tickers.csv', index=False)
# print(df)
