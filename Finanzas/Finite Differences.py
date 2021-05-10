import scipy.stats as si
import numpy as np
import pandas as pd
import scipy 
import numpy as np
import matplotlib.pyplot as plt

"""### Diferencias Finitas ###"""
#floating lookback EXPLICIT METHOD:

def BS_FTCS_lookback(S0, num_days, rf_rate, sigma, graph):
    var = sigma * sigma
    Tmax = num_days / 360
    Smax = int(1.2*S0)
    dt = 0.0001
    Stock = np.linspace(0,Smax,Smax+1)
    N = len(Stock)-1
    M = int(Tmax/dt)
    j = np.arange(0,N)
    
    #Creating the coefficients for the derivates aproximations    
    alpha = 0.5*(var*(j)**2-rf_rate*j)*dt            
    beta = 1-(var*(j)**2+rf_rate)*dt        
    gamma = 0.5*(var*(j**2)+rf_rate*(j))*dt    
    
    #Creating matrix of option price with boundary and terminal conditions
    P = np.zeros((M+1,N+1))
    
    #Condición de contorno
    P[:,-1]=0    #Derecha
    for j in range(0,M+1):
        P[j,0] = Smax*np.exp(-rf_rate*((M-j)*dt)) #Izquierda
        
    #Condición Terminal
    for i in range(N+1):
        P[M,i] = max(Smax-Stock[i],0)
        
    #Fill the matrix of prices by moving backward in the time        
    for i in range(M-1,-1,-1): #Time
        for j in range(N-1,0,-1): #Stock
            P[i,j]=alpha[j]*P[i+1,j-1]+beta[j]*P[i+1,j]+gamma[j]*P[i+1,j+1]
                
            
    if graph == True:
        plt.figure()
        for i in range(0,M,100):
            plt.clf()
            plt.xlabel('S')
            plt.ylabel('V(s,t)',fontsize=12)
            plt.title('Evolution as t moves to T')
            plt.suptitle('FTCS scheme for put option')
            plt.plot(Stock,P[i], color="red")
            plt.show()
            plt.pause(0.05)
    else:            
        mid_value = P[0, 100]    #fila 0 es tiempo 0;  columna 100 donde e el precio de la acción... 
        print('The Lookback put price is {} when stock is {}'.format(round(mid_value,3),round(Stock[100],3)))    
        
BS_FTCS_lookback(100, 30, 0.02, 0.4, graph= False)




#Plain Vanilla:

def BS_put(S0, strike, num_days, sigma, rf_rate):
    dt = num_days / 360     
    d1 = (np.log(S0/strike) + (rf_rate + sigma**2/2)*dt)/(sigma * np.sqrt(dt))
    d2 = d1 - sigma*np.sqrt(dt)
    put = strike * np.exp(-rf_rate*dt)*si.norm.cdf(-d2, 0, 1) - S0 * si.norm.cdf(-d1, 0, 1)        
    return put

BS_put(100, 105, 30, 0.2, 0.01)
        
def BS_explicit_put(S0, num_days, strike, rf_rate, sigma):
    var = sigma * sigma
    Tmax = num_days / 360
    Smax = 2*strike
    ds = 1
    dt = 0.0001
    Stock = np.linspace(0,Smax,Smax+1)
    N = len(Stock)-1
    M = int(Tmax/dt)
    j = np.arange(0,N)
    
    #Creating the coefficients for the derivates aproximations
    
    alpha = 0.5*(var*(j)**2-rf_rate*j)*dt            
    beta = 1-(var*(j)**2+rf_rate)*dt        
    gamma = 0.5*(var*(j**2)+rf_rate*(j))*dt    
    
    #Creating matrix of option price with boundary and terminal conditions
    P = np.zeros((M+1,N+1))
    
    #Condición de contorno
    P[:,-1]=0 # Derecha
    for j in range(0,M+1):
        P[j,0] = strike*np.exp(-rf_rate*((M-j)*dt)) #Izquierda
        
    #Condición Terminal
    for i in range(N+1):
        P[M,i] = max(strike-Stock[i],0)
        

    #Fill the matrix of prices by moving backward in the time
        
    for i in range(M-1,-1,-1): #Time
        for j in range(N-1,0,-1): #Stock
            P[i,j]=alpha[j]*P[i+1,j-1]+beta[j]*P[i+1,j]+gamma[j]*P[i+1,j+1]
                
    plt.figure()
    for i in range(0,M,100):
        plt.clf()
        plt.xlabel('S')
        plt.ylabel('V(s,t)',fontsize=12)
        plt.title('Evolution as t moves to T')
        plt.suptitle('FTCS scheme for put option')
        plt.plot(Stock,P[i], color="red")
        plt.show()
        plt.pause(0.05)
                
    mid_value = P[0, 100]    
    print('The put price is {} when stock is {} and strike {}'.format(round(mid_value,3),round(Stock[100],3),strike))
    print('The price by closed form BS is {}'.format(round(BS_put(S0,strike,num_days,sigma,rf_rate),3)))    
    return mid_value

BS_explicit_put(100, 30, 105, 0.03, 0.2)   
 


def BS_implicit_put(S0, num_days, strike, rf_rate, sigma):
    var = sigma * sigma
    Tmax = num_days / 360
    Smax = 2*strike
    dt = 0.0001
    N = int(Tmax/dt)
    Stock = np.linspace(0,Smax,int((Smax+1)))
    M = len(Stock)-1
    
    j = np.arange(0,M+1)
    i = np.arange(0,N+1)
    
    #Defino los coeficientes que acompañan a las derivadas
    a = 0.5*(-var*(j)**2+rf_rate*j)*dt            
    b = 1+(var*(j)**2+rf_rate)*dt        
    c = -0.5*(var*(j**2)+rf_rate*(j))*dt 
    
    P = np.zeros((M+1,N+1))
    
    #Condiciónes de contorno
    P[N:]=0 # S tiende a Smax
    for j in range(0,N+1):
        P[0,j] = strike*np.exp(-rf_rate*((N-j)*dt)) #S tiende a 0 
        
    #Condición Terminal
    for i in range(M):
        P[i,N] = max(strike-Stock[i],0)

    
    A = np.diag(a[2:M],-1) + np.diag(b[1:M])+np.diag(c[1:M-1],1) #Construyo la matriz e coeficientes
    [X,Y,Z]=scipy.linalg.lu(A) #Hago la descomposicion de las diagonales
    d = np.zeros(len(A)) #Creo el vector d

    for i in range(N-1,-1,-1):
        d[0] = -a[1]*P[0,i]
        d[-1] = -c[-1]*P[-1,i] 
        P[1:M,i] = np.linalg.solve(Z, np.linalg.solve(Y, (P[1:M,i+1]+d))) #Resuelvo las ecuaciones simulatenas 
        
    plt.title('Implicit scheme for put option')
    plt.xlabel('S') 
    plt.ylabel('V(s,t)',fontsize=12)
    plt.plot(Stock,P[:,0], color="red")
    
    mid_value = P[100,0]
    print('The put price is {} when stock is {} and strike {}'.format(round(mid_value,3),round(Stock[100],3),strike)) 
    print('The price by closed form BS is {}'.format(round(BS_put(S0,strike,num_days,sigma,rf_rate),3)))    
    
    return mid_value

BS_implicit_put(100, 30, 105, 0.01, 0.4)





