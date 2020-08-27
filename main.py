from yahoo_fin import options, requests
import pandas as pd
import pickle

tickers = pickle.load(open('list.pkl', 'rb'))

# replace DOW with DWDP in ticker list

# scrape the options data for each Dow ticker
for ticker in tickers:
    try:
        ticker_data = options.get_options_chain(ticker)
        ticker_df = pd.DataFrame(ticker_data["calls"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "call"
        ticker_df.to_csv("ticker.csv", mode="a", header=False, index=False)
        ticker_df = pd.DataFrame(ticker_data["puts"])
        ticker_df['Ticker Id'] = ticker
        ticker_df['Option Type'] = "put"
        ticker_df.to_csv("ticker.csv", mode="a", header=False, index=False)
    except Exception:
        print(ticker + " failed")

