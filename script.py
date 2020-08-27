# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:27:14 2020

@author: Liron
"""
import csv
from yahoo_fin import stock_info as si
from yahoo_fin import options
from time import gmtime, strftime
dow_tickers = si.tickers_dow()
nasdaq_tickers = si.tickers_nasdaq()
other_tickers = si.tickers_other()
spy_tickers = si.tickers_sp500()
# scrape the options data for all tickers
all_data = {}
for ticker in dow_tickers:
    try:
        all_data[ticker] = options.get_options_chain(ticker)
    except Exception:
        print(ticker + " failed")
for ticker in nasdaq_tickers:
    try:
        all_data[ticker] = options.get_options_chain(ticker)
    except Exception:
        print(ticker + " failed")
for ticker in spy_tickers:
    try:
        all_data[ticker] = options.get_options_chain(ticker)
    except Exception:
        print(ticker + " failed")
for ticker in other_tickers:
    try:
        all_data[ticker] = options.get_options_chain(ticker)
    except Exception:
        print(ticker + " failed")
        
import pickle
with open(("%Y-%m-%d%H:%M:%S", gmtime()) +'.pkl', 'wb') as handle:
    pickle.dump(all_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open(strftime("%Y-%m-%d%H:%M:%S", gmtime()) +'.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in all_data.items():
       writer.writerow([key, value])
print("done")