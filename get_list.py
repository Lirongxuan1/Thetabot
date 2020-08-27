import pandas as pd
import pickle

list = pd.read_csv('tickers.csv')

output = list['Ticker Id'].dropna().unique()
output = output.tolist()
pickle.dump(output, open('list.pkl','wb'))