import sys
import yfinance as yf 
import datetime
a = datetime.datetime(2020,2,2)
b= datetime.datetime(2020,2,3)
data=yf.download("7203.T",start='2020-02-02',end='2020-02-22')
