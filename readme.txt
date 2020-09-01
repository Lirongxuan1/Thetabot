This project is intended to automate trading strategies for selling options premiums.
fetch_data.py scrapes yahoo for stock info
generate_pairs.py creates sets of data points 
process_data.py processes data pairs and generates results
ALL Model inputs after processing (all are when opening a position): Tuples of Random Basic Data (single trade for cash covered puts/calls, one pair for Put Credit Spreads, two pairs for Iron Condor), gain/loss from each tuple, time taken for options to close, risk, Company sentiment, all the Greeks
