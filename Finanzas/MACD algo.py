#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:52:47 2020

@author: juanrossi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/jeron/Desktop/Proyectos Python/Finanzas/AAPL.csv')

def MACD(a, b, c):
    df['Ema1'] = df['Close'].ewm(span=a, adjust=False).mean()
    df['Ema2'] = df['Close'].ewm(span=b, adjust=False).mean()
    df['Macd'] = df['Ema1']-df['Ema2']
    df['Signal_line'] = df['Macd'].ewm(span=c, adjust=False).mean()

MACD(12, 26, 9)  

data = pd.DataFrame()
data['AAPL'] = df['Close']
data['Macd'] = df['Macd']
data['Signal_line'] = df['Signal_line']

plt.figure(figsize=(12.5, 4.6))
plt.plot(data['AAPL'], label = 'AAPL', color='Red')
plt.plot(data['Macd'], label='AAPL Macd', color = 'Orange')
plt.plot(data['Signal_line'], label='Signal line', color = 'Blue')
plt.legend(loc='upper left')
plt.show()

def buy_sell(data):
    sig_buy_price = []
    sig_sell_price = []
    flag = -1
    
    for i in range(len(data)):
        if data['Macd'][i] > data['Signal_line'][i]:
            if flag != 1:
                sig_buy_price.append(data['AAPL'][i])
                sig_sell_price.append(np.nan)
                flag = 1            
            else:
                sig_buy_price.append(np.nan)
                sig_sell_price.append(np.nan)
        elif data['Macd'][i] < data['Signal_line'][i]:
            if flag != 0:
                sig_buy_price.append(np.nan)
                sig_sell_price.append(data['AAPL'][i]) 
                flag = 0          
            else:
                sig_buy_price.append(np.nan)
                sig_sell_price.append(np.nan)
        else:
            sig_buy_price.append(np.nan)
            sig_sell_price.append(np.nan)
    return (sig_buy_price, sig_sell_price)

buy_sell = buy_sell(data)
data['Buy_signal_price'] = buy_sell[0]
data['Sell_signal_price'] = buy_sell[1] 

"""SIGNALS PLOT"""
plt.figure(figsize=(12.5, 4.6))
plt.plot(data['AAPL'], label='AAPL', alpha = 0.35)
plt.plot(data['Macd'], label='Macd', alpha = 0.35)
plt.plot(data['Signal_line'], label='Signal line', alpha = 0.35)
plt.scatter(data.index, data['Buy_signal_price'], label = 'Buy', marker = '>', color= 'green')
plt.scatter(data.index, data['Sell_signal_price'], label = 'Sell', marker = '<', color= 'red')
plt.title('Apple MACD buy and sell signals')

"""PERFORMANCE ANALISYS"""
b_s = buy_sell[0] + buy_sell[1]
trades = [b_s for b_s in b_s if str(b_s) != 'nan']
middle =int(len(trades)/2)
buy_trades = trades[0:middle]
sell_trades = trades[middle+1:]

pl = []
for i in range(len(sell_trades)):
    pl.append(buy_trades[i]-sell_trades[i])

prof = 0
non_prof = 0
for i in pl:   
    if i >= 0:
        prof += 1        
    else:
        non_prof += 1
    
print("The algo executed {} trades of which {} were profitable, the win ratio is {}".format(len(sell_trades), prof, prof/len(sell_trades) ))


