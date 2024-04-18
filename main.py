from flask import Flask,send_file,request,send_from_directory
import os
from app.route import *
import subprocess
from app import app

Country={'Japan':0,'NIKKEI':0,'DAX':1,'FTSE':2,'MIB':3,'TSX':4,'DJIA':5,'CAC':6}
ticker=[
        ['7203.T','6758.T','9432.T','8306.T','9984.T','9433.T','9983.T','4568.T','8035.T','4063.T','6501.T','6367.T','8058.T','8316.T','8001.T','4502.T','4519.T','8031.T','6902.T','8766.T','7267.T','2914.T','3382.T','8411.T','6954.T','4503.T','6702.T','5108.T','7733.T','9022.T'],
        ['SAP.DE','SIE.DE','DTE.DE','AIR.DE','VOW3.DE','ALV.DE','MRK.DE','MBG.DE','BMW.DE','BAYN.DE','DPW.DE','BAS.DE','MUV2.DE','IFX.DE','DB1.DE','HEN3.DE','RWE.DE','BEI.DE','SRT3.DE','EOAN.DE','HNR1.DE','ADS.DE','DBK.DE','PAH3.DE','SY1.DE','FRE.DE','ENR.DE','CON.DE','QIA.DE','MTX.DE','EBK.DE','VNA.DE','VTW0.DE','CBK.DE','LHA.DE','AFX.DE','TLX.DE','BNR.DE','FME.DE','RHM.DE','KBX.DE','ZAL.DE','DHER.DE','EVK.DE','HLE.DE','O2D.DE','DWNI.DE','PUM.DE','WCH.DE','O5G.DE','8TRA.DE','1COV.DE','G1A.DE','RAA.DE','NEM.DE','DWS.DE','EVD.DE','BC8.DE','SIX2.DE','LEG.DE','HOT.DE','FPE.DE','KGX.DE','FRA.DE','TKA.DE','BOSS.DE','SDF.DE','NDA.DE','G24.DE','LXS.DE','UTDI.DE','HFG.DE','KRN.DE','AT1.DE','HAG.DE','GIL.DE','SZU.DE','AIXA.DE','SUSE.DE','SAX.DE'],
        ['AZN.L','SHEL.L','ULVR.L','HSBA.L','RIO.L','DGE.L','BP.L','BATS.L','GLEN.L','GSK.L','REL.L','AAL.L','RKT.L','LSEG.L','NG.L','CPG.L','LLOY.L','PRU.L','EXPN.L','NWG.L','BA.L','VOD.L','BARC.L','CRH.L','AHT.L','FLTR.L','IMB.L','SSE.L','STAN.L','TSCO.L'],
        ['ENEL.MI','ENI.MI','STLA.MI','ISP.MI','STM.MI','G.MI','UCG.MI','CNHI.MI','TEN.MI','ATL.MI','SRG.MI','TRN.MI','CPR.MI','PRY.MI','REC.MI','MB.MI','DIA.MI','AMP.MI','BMED.MI','BAMI.MI','IP.MI','LDO.MI','TIT.MI','A2A.MI','HER.MI','BGN.MI','UNI.MI','BZU.MI','AZM.MI','BPE.MI'],
        ['RY','TD','CNR','ENB','CP','BAM-A','CNQ','BMO','BNS','TRI','ATD','BCE','NTR','SU','TRP','CM','CVE','WCN','MFC','CSU','IMO','T','ABX','L','FNV','SLF','IFC','RCI-B','NA','AEM'],
        ['AAPL','MSFT','UNH','JNJ','V','WMT','JPM','PG','CVX','HD','MRK','KO','CSCO','MCD','NKE','DIS','VZ','AMGN','HON','IBM','CRM','GS','CAT','INTC','AXP','BA','MMM','TRV','DD','WBA'],
        ['MC.PA','OR.PA','RMS.PA','TTE.PA','SAN.PA','AIR.PA','EL.PA','SU.PA','AI.PA','KER.PA','BNP.PA','CS.PA','DG.PA','SAF.PA','RI.PA','DSY.PA','STLA.PA','ENGI.PA','STM.PA','BN.PA','CAP.PA','ACA.PA','HO.PA','ORA.PA','SGO.PA','LR.PA','ML.PA','GLE.PA','VIE.PA','PUB.PA'] 
        ]

@app.route('/submit',methods = ['GET','POST'])
def submit():
    Index = request.form['select_menu']
    Date1 = request.form['date_input1']
    Date2 = request.form['date_input2']
    # return Date1+Date2
    return price_collect(app.root_path,Index+"_stockdata",ticker[Country[Index]],Date1,Date2)
    

@app.route('/works/<country>')
def works(country):
    return price_collect(app.root_path,"data",ticker[Country[country]],"2023-01-01","2023-01-31")

@app.route('/app/downloads/<filename>')
def downloads(filename):
    return download_file(app.root_path,filename)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

