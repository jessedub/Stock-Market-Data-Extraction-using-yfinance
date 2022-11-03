# Need to resolve yfinance install. Not working with Windows 8.1 and MSVS 14.0 Build Tools

# pip install yfinance
# pip install yfinance==0.1.67
# pip install yfinance --upgrade --no-cache-dir
# pip install yfinance==0.1.67 --upgrade --no-cache-dir
#!pip install pandas==1.3.3

import yfinance as yf
import pandas as pd

# Using the Ticker module we can create an object that will allow us to access functions to /
# extract data. To do this we need to provide the ticker symbol for the stock, /
# here the company is Apple and the ticker symbol is AAPL.

apple = yf.Ticker("AAPL")
zoom = yf.Ticker("ZM") # running the zoom examples after the prepopulated Apple program lines

# Using the attribute info we can extract information about the stock as a Python dictionary.

apple_info=apple.info
apple_info

zoom_info = zoom.info
zoom_info

# We can get the 'country' using the key country

apple_info['country']

zoom_info['country']

# Using the history() method we can get the share price of the stock over a certain period of time./
# Using the period parameter we can set how far back from the present to get data./
# The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.

apple_share_price_data = apple.history(period="max")
zoom_share_price_data = zoom.history(period = '10d')
zoom_share_price_data

apple_share_price_data.head()

zoom_share_price_data.head()

# We can reset the index of the DataFrame with the reset_index function./
# We also set the inplace paramter to True so the change takes place to the DataFrame itself.

apple_share_price_data.reset_index(inplace=True)

zoom_share_price_data.reset_index(inplace=True)

# We can plot the Open price against the Date:

apple_share_price_data.plot(x="Date", y="Open")

zoom_share_price_data.plot(x='Date',y='Open')

# Using the variable dividends we can get a dataframe of the data./
# The period of the data is given by the period defined in the 'history` function.

apple.dividends

# zoom.dividends # returns empty list because 5d period

# plot the dividends overtime:

apple.dividends.plot()

# new exercise below

# Now using the Ticker module create an object for AMD (Advanced Micro Devices) with the ticker symbol is AMD called; name the object amd.
adv_micro_devices = yf.Ticker("AMD")
adv_micro_devices

# Use the key 'country' to find the country the stock belongs to, remember it as it will be a quiz question.
adv_micro_devices_info = adv_micro_devices.info
#adv_micro_devices_info
adv_micro_devices_info["country"]

# Use the key 'sector' to find the sector the stock belongs to, remember it as it will be a quiz question.
adv_micro_devices_info["sector"]

# Obtain stock data for AMD using the history function, set the period to max. Find the Volume traded on the first day (first row).
AMD_price = adv_micro_devices.history(period="max")
print("First AMD trading day Volume =",AMD_price.iloc[0,4])
AMD_price.head()

