# Part 5
# S&P 500  and the company´s it comprises (top 500 co's in  MARKET CAP / Value)

# go to s$p list of co's in wikipwdia ;  ctrl + U to go to source ; find th ebeggining of "Table"
# you should find :   "<table class="wikitable sortable" id="changes">"
# now we will use beautifullsoup to pull apart the table : import it :
from datetime import datetime
from typing import List, Any

import bs4 as bs
import pickle  # to save any object.... in this case the s&p list
import requests
import sys

import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

import datetime as dt
import os  # to create new directories
import pandas as pd
import pandas_datareader as web
from pandas.util.testing import assert_frame_equal

sys.setrecursionlimit(100000)


def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')  # this is original Wiki page
    soup = bs.BeautifulSoup(resp.text, features='lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []  # an empty ticker list
    tickers_clean = []  # La creé para sacar el \n desp de cada ticker !!!!!!!!!!!!! mirar linea 26
    for row in table.findAll('tr')[1:]:  # tr for Table Row, [1: onward because the firts row is a header we dont need
        ticker = row.findAll('td')[
            0].text  # tickers are in the fist column .text to make soup object a string for python
        tickers.append(ticker)
    for ele in tickers:  # forma de sacarle el n a cada string de la lista
        tickers_clean.append(ele.strip())
    # to save the list
    with open("sp500tickers.pickle", "wb") as f:  # save the full tickers list wb = write bites
        pickle.dump(tickers_clean, f)
    print(tickers_clean)
    return tickers_clean


# save_sp500_tickers()

# video 6 ...sigue
# saving the data of the company's
print('\n')


def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:  # we arent gonna write bytes.. bur Read b
            tickers = pickle.load(f)
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')  # acá creamos una carpeta q se guarda en el proyecto con los tickers .csv

    start = dt.datetime(2017, 1, 1)
    end = dt.datetime(2019, 12, 31)

    for ticker in tickers:  # here you can put [:50] for the firts 50 co´s...

        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start=start, end=end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))  # to create the csv ´s
        else:
            print('Already have {}'.format(ticker))


# get_data_from_yahoo()

# video 7
# combinign all the stocks csv's together
def compile_data():
    with open("sp500tickers.pickle", "rb")as f:
        tickers = pickle.load(f)
        # now ready to begin creating our DF
    main_df = pd.DataFrame()
    for count, ticker in enumerate(tickers):
        df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)

        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')
        if count % 10 == 0:  # someting divided by 10 (modulo) if the remainder is 0...
            print(count)
    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')


# compile_data()

print('\n')

# Video 8
#for a CORRELATION graph
style.use('ggplot')


def visualize_data():
    df = pd.read_csv('sp500_joined_closes.csv')
    #   df['AAPL'].plot()
    #   plt.show()
    df_corr = df.corr()  # WILL CREATE THE CORRELATION TABLE.. THE VALUES !!!
    print(df_corr.head())

    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)  # it means its a 1X1 with plot #1

    # creating a heat map :
    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0] + 0.5))  # x ticks at every 0.5
    ax.set_yticks(np.arange(data.shape[1] + 0.5))  # y ticks  at every1.5
    ax.invert_yaxis()
    ax.xaxis.tick_top()  # to put the x axis on the top

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    heatmap.set_clim(-1, 1)  # limit of the colour of the heats  from -1 to 1
    plt.tight_layout()  # to clean things up...
    plt.show()


#visualize_data()
