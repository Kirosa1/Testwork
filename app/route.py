from flask import render_template,send_from_directory,send_file
from app.script import test
import os
import yfinance as yf
import pandas as pd

macro={}
macro.update({"DOWNLOAD_FOLDER": "downloads"}) 
macro['DOWNLOAD_FOLDER'] = 'downloads'

slide = {'Y2Y':0,'Y2H':1,'Y2Q':2,'Y2M':3,'H#':4,'H2H':5,'H2Q':6,'H2M':7,'Q#':8,'Q2Q':9,'Q2M':10,'M#':11,'M2M':12}
slide_month=[
    []
]
def hello_world():
    return "MVC框架!"

def rendering():
    return render_template('index.html')

def download_file(rootpath,filename):
    filepath = os.path.join(rootpath, macro['DOWNLOAD_FOLDER'])
    return send_from_directory(filepath,filename,as_attachment=True)
    #return filepath+filename

def price_collect(ROUTE,FILENAME,TICKER,start,end):
    year_start = start.split('-')[0]
    year_end = end.split('-')[0]
    
    if(len(TICKER)>0):
        data=yf.download(TICKER,start,end)
        path = os.path.join(ROUTE,macro['DOWNLOAD_FOLDER'])
        csvdata  = data['Close'].to_csv(os.path.join('app',macro['DOWNLOAD_FOLDER'],FILENAME+'.csv'))
        return send_from_directory(path,FILENAME+'.csv',as_attachment=True)
        df = data['Close']
        for year in range(year_start,year_end+1):
            for month in range(1, 13,):  # 从1到12遍历每个月份
                start_date = f'{year:04d}-{month:02d}-01'  # 生成每个月份的开始日期，例如 '2023-01-01'
                end_date = pd.date_range(start=start_date, periods=2, freq='M').max()  # 生成每个月份的结束日期
                slice_data = df[start_date:end_date]  # 使用切片操作获取该月份的数据        
        
        
        

    
