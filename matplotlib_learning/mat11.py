print('Working with subplots')

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn-v0_8')

data = pd.read_csv('matplotlib_learning\data (1).csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig,(ax1,ax2)=plt.subplots(nrows=2,ncols=1,sharex=1)#sharex used for sharing two axis i.e,x

ax1.plot(ages, py_salaries, label='Python')
ax1.plot(ages, js_salaries, label='JavaScript')

ax1.legend()

ax1.set_title('Median Salary (USD) by Age')
#ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

ax2.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax2.legend()

#ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
fig.savefig('subplots.jpeg')
#in case of saving more than two fig images just use this
#fig1.savefig('fig1.png')
#fig2.savefig('fig2.png')