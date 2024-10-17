print("working with histogram")
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('matplotlib_learning\data (2).csv')
ids = data['Responder_id']
ages = data['Age']

bin=[10,20,30,40,50,60,70]

plt.hist(ages,bins=5,edgecolor='black',log=True)  #log is used to show data in logrithmic way

median_age = 29
color = '#fc4f30'

plt.axvline(median_age,color=color,label='Age Median',linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()