#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 31 05:46:27 2025
reads and plots fsrs_hourly_1999_2000 color coded by site
@author: user
"""
from pandas import read_csv,to_datetime
from matplotlib import pyplot as plt
import numpy as np

df= read_csv('fsrs_hourly_1999_2000.csv')
df['datet']=to_datetime(df['datet'])
df.set_index('datet',inplace=True)
df=df[df.temp!=-99.0]
df=df[df.lat!=-99.0]
sites=np.unique(df['lat']) # this is how we can split up the sites assuming there is no sites with exactly the same lat

fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot(111)
for k in sites:
    df1=df[df['lat']==k]
    df1['diff']=df1.index.diff()
    id=np.where(df1['diff'].astype('timedelta64[s]').dt.days>20)#looks for >20 days breaks in the data
    if len(id[0])>0:
        #ax.plot(df1.index[id],df1['temp'][id[0]],'r.',markersize=50)
        #df1=df1[df1.index!=df1.index[id[0][0]]]
        df1['temp'][id[0]]=np.nan
    ax.plot(df1.index,df1['temp'])

