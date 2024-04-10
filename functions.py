import yfinance as yf
import pandas as pd
yf.pdr_override();

def get_data(symbol):
    data = yf.download(tickers=symbol.name, period=symbol.period,  start=symbol.start_date, end=symbol.end_date)
    data.reset_index(inplace=True)
    data.rename(columns={'index': 'date'}, inplace=True)
    return data
