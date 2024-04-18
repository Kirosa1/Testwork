import yfinance as yf
import pandas as pd
#ticker=["7203.T","6758.T","9432.T","8306.T","9984.T","9433.T","9983.T","4568.T","8035.T","4063.T","6501.T","6367.T","8058.T","8316.T","8001.T","4502.T","4519.T","8031.T","6902.T","8766.T","7267.T","2914.T","3382.T","8411.T","6954.T","4503.T","6702.T","5108.T","7733.T","9022.T"]
def price_collect(ROUTE,FILENAME,TICKER,start,end):

    filename = FILENAME
    if(len(TICKER)>0):
        data=yf.download(TICKER,start,end)
        data['Close'].to_csv('./app/dowloads/'+FILENAME+'.csv')
        return data['Close']
        

        
