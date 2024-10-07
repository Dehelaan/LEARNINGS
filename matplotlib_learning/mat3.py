print('working with csv files')
import csv
from collections import Counter
import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

with open('matplotlib_learning\data.csv') as csv_file: 
    csv_reader = csv.DictReader(csv_file)  # method to read a csv file without pandas

    language_counter = Counter() #created a variable to store counted values

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';')) #updating each values as loop goes on

    #row = next(csv_reader)
    #print(row['LanguagesWorkedWith'].split(';')) #giving a list of first row in csv
#print(language_counter.most_common(10)) #counting most common 10 values and storing them in list of tuple
axis_x=[]
axis_y=[]
for item in language_counter.most_common(10):
    axis_x.append(item[0])
    axis_y.append(item[1])

#print(axis_x,axis_y)
axis_x.reverse()  #for reversing x and y axis
axis_y.reverse()
plt.barh(axis_x,axis_y,label="top 10 most common",color='#444444') #.barh to make graph horizontal
plt.title('top 10 most common')
plt.xlabel('languages')
plt.ylabel('counter')
plt.tight_layout()
plt.legend()
plt.show()