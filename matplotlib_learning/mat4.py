from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

#parts=[82,74,82,62,74]
#label=['one','two','three','four','five']
color=['#003F5C','#58508D','#BC5090','#FF6361','#FFA600']

# note: try using pie chart only for less no. of attributes or features for ex- 5 or 6
# Language Popularity
parts = [59219, 55466, 47544, 36443, 35917]
label = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode =[0,0,0,0.2,0]  #used to explode or bringout that part of the pie chart out


plt.pie(parts,labels=label,colors=color,explode=explode,wedgeprops={'edgecolor':'black'},shadow=True,startangle=90,autopct='%1.1F%%') #shadow for shadow,starangle used for rotating graph to a certain angle,autopact gives automatically the ppercentage part of the piece of the graph
plt.title("Pie charts")
plt.tight_layout()
plt.show()