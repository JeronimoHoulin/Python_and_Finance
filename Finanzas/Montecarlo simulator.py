import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def monte_carlo(S0, sigma, num_days, rf_rate, num_trials, graph):
    T = num_days/360
    dt = T/num_days # MONITOREO DIARIO dt = 1/360

    simulation_df= pd.DataFrame()   #pandas te arma una matriz.
    
    for x in range(num_trials):
        price_series = [S0]                    
        for i in range(num_days):
            price = price_series[-1] * np.exp((rf_rate - 0.5*sigma**2)*dt + sigma * np.random.normal(0, 1) * np.sqrt(dt))
            price_series.append(price)  
            
        simulation_df[x] = price_series
        
    if graph == True:
        fig = plt.figure()
        fig.suptitle('Montecarlo Simulation')
        plt.plot(simulation_df)
        plt.xlabel('day')
        plt.ylabel('price')
        plt.show()
    
    if graph == False:
        return print("{} Is the avergae predicted price in expiration !".format(round(sum(simulation_df.loc[num_days]) / num_trials, 4))) 

monte_carlo(100, 0.2, 40, 0.01, 100, graph= False)




