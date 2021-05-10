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
from pandas.testing import assert_frame_equal
from collections import Counter
#video 12 de ML :
from sklearn import svm, neighbors
from sklearn.model_selection import cross_validate
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

# video 9
# correlation with machin learning / AI

# proces data into percentages...

def process_data_for_labels(ticker):
    hm_days = 7  # time frame (precent changes in the next week)
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days + 1):
        df['{}_{}d'.format(ticker, i)] = (
                df[ticker].shift(-i) - df[ticker] / df[ticker])  # (new - old) / old ....  %change
    df.fillna(0, inplace=True)
    return tickers, df


# process_data_for_labels('XOM')


# video 10
# Target function for ML
# new column for target function (buy, hold or sell)

def buy_sell_hold(*args):  # args is to less pas any number of arguments..
    cols = [c for c in args]
    requirement = 0.02  # if stock price moves by 2% we either buy of sell
    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
        return 0  # so 1 is a buy, -1 is a sell, a 0 is a hold


# video 11
# mapping out these columns

def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)

    df['{}_target'.format(ticker)] = list(map(buy_sell_hold,
                                              df['{}_1d'.format(ticker)],
                                              df['{}_2d'.format(ticker)],
                                              df['{}_3d'.format(ticker)],
                                              df['{}_4d'.format(ticker)],
                                              df['{}_5d'.format(ticker)],
                                              df['{}_6d'.format(ticker)],
                                              df['{}_7d'.format(ticker)]))
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread:', Counter(str_vals))

    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)  # for prices that hit zero not to cause a % problem
    df.dropna(inplace=True)

    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)
    # X = feature sets that describe the target; y = labels / target / class
    x = df_vals.values
    y = df['{}_target'.format(ticker)].values

    return x, y, df


#extract_featuresets("XOM")
# video 12
#running Machine Learning
def do_ml(ticker):
    x, y, df = extract_featuresets(ticker)
    #create our training & testing
    x_train, x_test, y_train, y_test, = cross_validate().train_test_split(x, y, test_size= 0.25)
    clf = neighbors.KNeighborsClassifier()
    clf.fit(x_train, y_train)
    # remember; x is % change for all companys, and y is target, 0, 1 or -1 for hold, buy, sell
    confidence = clf.score(x_test, y_test)
    predictions = clf.predict(x_test)

    print('Predicted spread: ', Counter(predictions))
    return confidence

do_ml('BAC')
