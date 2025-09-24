# Derivatives_Analytics
Data Analysis, Models, Simulation, Calibration and Hedging


# VOLATILITY AND CORRELATION
Volatility may be the most central notion in option and derivatives analytics. There is not a simple volatility concept but rather a family of concepts related to the notion of an "undirected dispersion/risk measure". Books distinguish between the following volatility concepts:

* **Historical volatility:** this refers to the standard deviation of log returns of a financial time series; suppose we observe N (past) log returns $r_n , n \in{1,...,N}$ , 

<p align="center">$\hat\mu = \frac{1}{N} \sum_{n=1}^{N} r_n$</p>

with mean return the historical volatility $\hat\sigma$ in then given by 

<p align="center">$\hat\sigma = \sqrt{ \frac{1}{N-1} \sum_{n=1}^{N}(r_n - \hat\mu)^2}$</p>

* **Instantaneous volatility:** this refers to the volatility factor of a diffusion process; for example, in the Black-Scholes-Merton model the instantaneous volatility $\sigma$ is found in the respective (risk-neutral) Stochastic Differential Equiation (SDE).

<p align="center">$dS_t = rS_t dt + \sigma S_t dZ_t$</p>

* **Implied Volatility:** this is the volatility that, if put into the Blacj-Scholes-merton option pricing formula, gives the market observed price of an option; suppose we observe today a price of $C_{0}^{*}$ for an European call option; the implied volatility $\sigma^{imp}$ is the quantity that solves ceteris paribus the implicit equation.

<p align="center">$C_{0}^{*} = C^{BSM} (S_0, K, T, r, \sigma^{imp})$</p>

This volatilities all have squared counterparts wich are then named *variance*. For example, in some financial models where volatility is stochastic, in constrast to the BMS assumption, the variance is modeled instead of the volatility.

