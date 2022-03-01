"""
STOCK MARKET DATA ANALYSIS USING PYTHON 
"""
import pandas as pd
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix



Reliance_industries = pdr.get_data_yahoo('RELIANCE.NS',
                          start = datetime.datetime(2019,1,1),
                          end = datetime.datetime(2020,1,1))
Hdfc_bank = pdr.get_data_yahoo('HDB',
                          start = datetime.datetime(2019,1,1),
                          end = datetime.datetime(2020,1,1))
Trident = pdr.get_data_yahoo('TRIDENT.NS',
                             start = datetime.datetime(2019,1,1),
                             end = datetime.datetime(2020,1,1))
                            
type(Reliance_industries), type(Hdfc_bank), type(Trident)

"""
Showing Opening ,Closing, High prices, Low prices for year 
2019-2020 of Relaince_Industries Shares.
"""

Reliance_industries.head()
Reliance_industries['Open'].plot(label = "Reliance_industries - open_prices")
Reliance_industries['Close'].plot(label = "Reliance_industries - close_prices")
Reliance_industries['High'].plot(label = "Reliance_industries - High_prices")
Reliance_industries['Low'].plot(label = "Reliance_industries - low_prices")

plt.title('Reliance Share Analysis')
plt.ylabel('Share price')

"""
Showing Opening ,Closing, High prices, Low prices for year 
2019-2020 of HDFC Bank Shares.
"""
"""
Hdfc_bank['Open'].plot(label = "HDFC Bank - open_prices")
Hdfc_bank['Close'].plot(label = "HDFC Bank - close_prices")
Hdfc_bank['High'].plot(label = "HDFC Bank - High_prices")
Hdfc_bank['Low'].plot(label = "HDFC Bank - low_prices")

plt.title('HDFC Bank Share Analysis')
plt.ylabel('Share price')
"""

"""
Showing Opening ,Closing, High prices, Low prices for year 
2019-2020 of Trident ltd Share.
"""

"""
Trident['Open'].plot(label = "Trident - open_prices")
Trident['Close'].plot(label = "Trident - close_prices")
Trident['High'].plot(label = "Trident - High_prices")
Trident['Low'].plot(label = "Trident - low_prices")

plt.title('Trident Share Analysis')
plt.ylabel('Share price')
"""

"""
shwoing total traded amount for Trident ltd Share.
"""

"""
Trident['Total traded'] = Trident['Open'] * Trident['Volume']
Trident['Total traded'].plot(label='Trident')
Trident.head
"""

"""
comparison between all the 3 shares
(Reliance, HDFC Bank and Trident)
"""

"""
Reliance_industries['Open'].plot(label = "Reliance_industries - open_prices")
Hdfc_bank['Open'].plot(label = "HDFC Bank - open_prices")
Trident['Open'].plot(label = "Trident - open_prices")
plt.legend()
plt.show()
"""
"""
Trident['Close'].plot(label = "Trident - close_prices")
Hdfc_bank['Close'].plot(label = "HDFC Bank - close_prices")
Reliance_industries['Close'].plot(label = "Reliance_industries - close_prices")
plt.legend()
plt.show()
"""
"""
showing relation betwen shares()
"""

"""
Stock_Share = pd.concat([Reliance_industries['Open'],Hdfc_bank['Open'],Trident['Open']],axis = 1)
scatter_matrix(Stock_Share)
"""
"""
Return that are provided by the specific share on daily basis
"""

Reliance_industries["Returns"] = (Reliance_industries['Close']/Reliance_industries['Close'].shift(1))-1
Hdfc_bank["Returns"] = (Hdfc_bank['Close']/Hdfc_bank['Close'].shift(1))-1
Trident["Returns"] = (Trident['Close']/Trident['Close'].shift(1))-1


"""
Plotting them in histogram
"""

"""
Trident['Returns'].hist(bins = 100,label ='Trident',alpha =0.5 )
Hdfc_bank['Returns'].hist(bins = 100,label ='HDFC Bank',alpha =0.5)
Reliance_industries['Returns'].hist(bins = 100,label ='Reliance',alpha =0.5)
"""

"""
plotting them in line graph
"""
"""
Trident['Returns'].plot(label ='Trident' )


Hdfc_bank['Returns'].plot(label ='HDFCBank')


Reliance_industries['Returns'].plot(label ='Reliance')
"""