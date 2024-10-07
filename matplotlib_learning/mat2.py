print('Working with Bar Charts')
import numpy as np
from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")
side_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
x_indexes = np.arange(len(side_x)) #since our bars werew overlaping , so in order to make them side by side we have used to store all the side_y's in adjacent to each other thus we have used numpy arrange function
width = 0.25 #default width of the bar is 0.8 we changed itto 0.25 so that side_y's can be plotted side by side.Also made width = width in bar defination

side_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]
#plt.plot(side_x, side_y,color='#444444',label='PYTHON DEV') #Line Graph
plt.bar(x_indexes-width, side_y,width =width,color='#444444',label='PYTHON DEV') #Bar Chart Graph
side_y2 = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
plt.bar(x_indexes,side_y2,width=width,color='#5a7d9a',linestyle='--',label='JS DEV')
side_y3 = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]
plt.bar(x_indexes+width,side_y3,width=width,color='#adad3b',linestyle='-.',label='OTHER DEV')
plt.legend()

plt.xticks(ticks=x_indexes,labels=side_x) #we have used the tick method so that we can allign all the x index with their respective graphs
plt.title('Median Salary by ages(USA)')
plt.xlabel('ages')
plt.ylabel('Median Salary')
plt.tight_layout()
plt.show()


