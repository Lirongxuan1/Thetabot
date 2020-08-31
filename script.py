# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:27:14 2020

@author: Liron
"""
import csv
from yahoo_fin import stock_info as si
from yahoo_fin import options
from time import gmtime, strftime
import pickle

# scrape the options data for all tickers
all_data = {}
tickers = pickle.load(open('list.pkl', 'rb'))
# scrape the options data for each Dow ticker


for ticker in tickers:
    try:
        all_data[ticker] = options.get_options_chain(ticker)
    except Exception:
        print(ticker + " failed")
        
with open(("%Y-%m-%d%H:%M:%S", gmtime()) +'.pkl', 'wb') as handle:
    pickle.dump(all_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open(strftime("%Y-%m-%d%H:%M:%S", gmtime()) +'.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in all_data.items():
       writer.writerow([key, value])
print("done")