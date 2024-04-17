import json
import sys
import yfinance as yf
import datetime
import requests as req
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
import csv
import pandas_datareader as pdr
#ticker=["7203.T","6758.T","9432.T","8306.T","9984.T","9433.T","9983.T","4568.T","8035.T","4063.T","6501.T","6367.T","8058.T","8316.T","8001.T","4502.T","4519.T","8031.T","6902.T","8766.T","7267.T","2914.T","3382.T","8411.T","6954.T","4503.T","6702.T","5108.T","7733.T","9022.T"]

requirement = 4
if(len(sys.argv)>requirement):
    filename = sys.argv[1]
    ticker = []
    for stocks in sys.argv[2].split(','):
        ticker.append(stocks)
    table = []
    day = 0

    if(len(ticker)>0):
        data=yf.download(ticker[0],sys.argv[3],sys.argv[4])
        day  = len(data['Close'])
        table.append([])
        for i in ticker:
            table[0].append(i)
        for i in ticker:
                data=yf.download(i,sys.argv[3],sys.argv[4])
                j=0
                for k in data['Close']:
                    table[j].append(k)
                    j=j+1

        with open(filename,'w',newline='') as csvfile:
                write = csv.writer(csvfile)
                write.writerows(table)

        print(filename)
