# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 09:14:21 2016

@author: Hou Haowen
"""
import HP4156A
import datetime
import pandas as pd
import numpy as np

my4156=HP4156A.HP4156A()
my4156.open_connection("GPIB0::2::INSTR")

V=[]
I=[]
V,I=my4156.dataAcquisition(['VF','IF']) #two terminal

date=datetime.datetime.now()
date_str=date.strftime('%Y-%m-%d %H_%M')
file_path=r'C:\Users\Hou Haowen\Documents\My Research\SMART project\python for test and measurement\Python_data'
data_name="_LED I-V"
file_name=file_path+ "\\" +date_str + data_name + ".csv"

udata_fields=['Voltage','Current']
ndata=np.array([V,I])
ndata=np.transpose(ndata)
udata=pd.DataFrame(ndata,index=range(1,len(V)+1),columns=udata_fields)
udata.to_csv(file_name, sep=',', encoding='utf-8')