import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn-v0_8')



"""plt.gcf().autofmt_xdate    #get current figure

date_format = mpl_dates.DateFormatter('%b, %d , %Y')
plt.gca().xaxis.set_major_formatter(date_format)  #get current axis"""


data = pd.read_csv('time_series_data.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace = True) # or data = date.sort('Date', inplace= True)

price_date = data['Date']
price_close = data['Close']


plt.plot_date(price_date, price_close, linestyle = 'solid')
plt.gcf().autofmt_xdate()


plt.tight_layout()
plt.show()