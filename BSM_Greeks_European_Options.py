# -*- coding: utf-8 -*-
"""
Back-Schales-Merton Call Greeks
"""
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'
import mpl_toolkits.mplot3d.axes3d as p3
from scipy.integrate import quad

def dN(x):
    return math.exp(-0.5*x**2)/ math.sqrt(2 * math.pi)

def N(d):
    return quad(lambda x: dN(x), -20, d, limit=50)[0]

def d1f(St, K, t, T, r, sigma):
    d1 = (math.log(St / K) + (r + 0.5 * sigma **2)
          * (T-t)) / (sigma * math.sqrt(T-t))
    return d1




def BSM_delta(St, K, t, T, r, sigma):
    '''Black scholes Metton Delta of European call option.
    Parameters
    ====
    St: float
        stock/index level at time t (spot)
    K: float
        strike price
    t: float
        Value date
    T: float
        Date to maturity/ time to maturity if t = 0; T>t
    r: float 
        constant, risk-less short rate
    sigma: float
        volatility
    
    Returns
    ===
    delta: float
        European call option Delta
    '''
    d1 = d1f(St, K, t, T, r, sigma)
    delta = N(d1)
    return delta

def BSM_gamma (St, K, t, T, r, sigma):
    d1 = d1f(St, K, t, T, r, sigma)
    gamma = dN(d1)/(St*sigma*math.sqrt(T-t))
    return gamma

def BSM_theta(St, K, t, T, r, sigma):
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T-t)
    theta = -(St * dN(d1) * sigma/ (2*math.sqrt(T-t)) + 
              r * K * math.exp(-r * (T-t)) * N(d2))
    return theta

def BSM_rho(St, K, t, T, r, sigma):
    d1 = d1f(St, K, t, T, r, sigma)
    d2 = d1 - sigma * math.sqrt(T-t)
    rho = K * (T-t) * math.exp(-r * (T-t)) * N(d2)
    return rho


def BSM_vega(St, K, t, T, r, sigma):
    d1 = d1f(St, K, t, T, r, sigma)
    vega = St * dN(d1) * math.sqrt(T-t)
    return vega


#Plotting Greeks
def plot_greeks(function, greeks):
    # Model Parameters
    St = 100.0
    K = 100.0
    t = 0.0
    T = 1
    r = 0.05
    sigma = 0.2
    
    #Greeks Calculations
    tlist = np.linspace(0.01, 1, 25)
    klist = np.linspace(80, 120, 25)
    V = np.zeros((len(tlist), len(klist)), dtype = np.float)
    for j in range(len(tlist)):
        V[i,j] = function(St, klist[j], [j], t, tlist[i], r, sigma)
        
    ##3d plot
    x, y = np.meshgrid(klist, tlist)
    fig = plt.figure(figsize=(9,5))
    plot = p3.Axes3D(fig)
    plot.plot_wireframe(x, y, V)
    plot.set_xlabel('strike $K$')
    plot.set_ylabel('maturity $T$')
    plot.set_zlabel('%s(K,T)' % greek)