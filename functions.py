import yfinance as yf
import pandas as pd

from pandas_datareader import data as pdr
yf.pdr_override()

def get_data(name):
    data = yf.download(name, period="3mo")
    data.reset_index(inplace=True)
    data.rename(columns={'index': 'date'}, inplace=True)
    return data
