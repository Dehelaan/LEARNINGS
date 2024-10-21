print('Working with time series plots')
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates # to change the dates in a specific date format

plt.style.use('seaborn-v0_8')

#dates = [
#    datetime(2019, 5, 24),
#    datetime(2019, 5, 25),
 #   datetime(2019, 5, 26),
 #   datetime(2019, 5, 27),
 #   datetime(2019, 5, 28),
 #   datetime(2019, 5, 29),
  #  datetime(2019, 5, 30)
#]

#y = [0, 1, 3, 4, 6, 5, 7]

#plt.plot_date(dates,y, linestyle='solid') #linestyle=solid is used to connect dots


date_format = mpl_dates.DateFormatter('%d %b ,%Y')  #Specifing the format of thed date https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa204X0xWTGJBNXE2VnR5V0luSEplWjdwR29YQXxBQ3Jtc0tsRm9tOFVjMnRJRTJUX2lPNmRsVGtyUnd1VG9ja3hnTzNvS1BoT0R1TTlMdVpncFRJUjh1TXg1QmNMX015ZVZZYll0ZG1MOEhCTlZMb0RURkI4QzZka0w1WEg0M2N3T2JUR2FnRHMyVWFoNjExR1VJaw&q=http%3A%2F%2Fbit.ly%2Fpython-dt-fmt&v=_LWjaAiKaf8

plt.gca().xaxis.set_major_formatter(date_format) #to set the dates format



data = pd.read_csv('matplotlib_learning\data (3).csv')
price_date = data['Date']
price_close = data['Close']


data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

plt.plot_date(price_date,price_close,linestyle ='solid')

plt.gcf().autofmt_xdate() # to change or rotate the dates in the graph


plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()