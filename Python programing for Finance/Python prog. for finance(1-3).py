#1st meke sure interpreter is python38 and not python project file..
#canot pip install from here; from cmd plain
#to grab data:
import datetime as dt
import matplotlib.pyplot as plt #plots, charts... with style good lookin
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web #to grab data from yahoo fin api

style.use('ggplot')
''' read line20 ...
start = dt.datetime(2017,1,1)
end = dt.datetime(2019,12,31)  #( yr, month, day)
#dataframe = df
df = web.DataReader('TSLA', 'yahoo', start, end)  #yahoo /
print(df.head(20))  #only prints out FIRST 5 (if you dont put any nbrs in the brakts) rows of our dataframe
#because of .head ... if LAST n ronw    .tail
#adj. close is adjustment for stock splits, halving...etc.

df.to_csv('tsla.csv') # turn df into csv ... an excel
#now you can use this file and cancel out.. or comment out all other commands
'''

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
'''
print(df.head())
df['Adj Close'].plot()
plt.show() #to show the graph.... its too much with the volume.. so  back to line 26 put Adj Close
'''

#print(df[['Open', 'High']])


#video 3 stock data manipulation
#df ['100ma'] = df['Adj Close'].rolling(window=100).mean()    #today´s 100 moving average take 99 prices before and avrg them
#print(df.head())
# it only aded a column to our data frame of NaN, because we used head.. not 99 data behined
#print(df.tail())    #now column 100ma makes sense

#drop n a function  para que .head si funcione (larga 100 dias para que no hayan NaN
'''
df.dropna(inplace=True)   #inplace is to not do df = df.dropna
print(df.head())
'''

#Another way to do an avrg of the price as the days go by =
df ['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
print(df.head())
'''
graphing
to have many "subplots" in one graph, which are called axis, you have to 1st create each axis
'''
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)  #1st parameter = grid size ; 2nd = starting point ; 3rd = how many rows its gonna soan
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1, sharex=ax1) #sharex=ax1 so that volume isnt separeted from price...

ax1.plot(df.index, df['Adj Close'])  #x axis should be the date, and Y adj close
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])
plt.show()


#part 4  .. no me salió nada
import mplfinance as mplf    #NOSE COMO USAR ESTO
import matplotlib.dates as mdates

'''
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
df_ohlc = df['Adj Close'].resample('10D').ohlc()   #.resample(10D) cpuld be 6min .. 1month... open higl low close
df_volume = df['Volume'].resample('10D').sum()   # sum (true volume over 10D not avrg.. makes more sense

#print(df_ohlc.head())

#now to use matplot lib´s  CANDLE STICK ... LINES 7 & 8
#Candlestick_ohlc needs  dates (in mdates format) and o h l c
df_ohlc.reset_index(inplace=True)
df_ohlc['Datetime'] = pd.to_datetime(df_ohlc['Date'])
df_ohlc = df_ohlc.set_index('Datetime')    #creo q ndad de testo va...
df_ohlc = df_ohlc.drop(['Date'])          #el formato de Date ya está en pandas Datime format
print(df_ohlc.head())

ax1.xaxis_date()

mplf.plot(df_ohlc)
ax2.fill_between(df_volume.index.map(mdates.dates2num), df_volume.values, 0)

'''