import sys
import yfinance as yf 
import datetime

import csv
a = datetime.datetime(2020,2,2)
b= datetime.datetime(2020,2,3)
ine = ["7203.T","6758.T"]
data=yf.download(ine,start='2020-02-02',end='2020-02-22')
data=data['Close']
print(data.index)
#data.to_csv('./app/downloads/iedjejdwedw.csv')
