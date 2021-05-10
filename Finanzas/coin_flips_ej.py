# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:21:13 2020

@author: jeron
"""
# coin flipperr
#random module:
#https://www.youtube.com/watch?v=KzqSDvzOFNA
import random


simulations_ran = 0
average = []
while simulations_ran <= 10:
    
    def coin_toss():
        if random.randint(0,1) == 1:
            return "H"
        else:
            return "T"
    
    list_of_tosses = []
    for _ in range(3):
        list_of_tosses.append(coin_toss())
        print(list_of_tosses)
    
    while not len(set(list_of_tosses[-3:]))==1:
        list_of_tosses.append(coin_toss())
        print(list_of_tosses)
    
    print("Three in a row!")
    print("It took: " + str(len(list_of_tosses))+" tosses to get three consecutive H / T")
    
    simulations_ran +=1
    average.append(int(len(list_of_tosses)))
print("The average tosses needed, in 10 simulations, to get three consecutive T/H was:  " + str(sum(average)/10) + " tosses.")







