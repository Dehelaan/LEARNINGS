print("working with Stack plots")
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

label=['player1','player2','player3']
color=['#003F5C','#58508D','#BC5090']

#plt.pie([1, 1, 1], labels=["Player 1", "Player2", "Player3"])
plt.stackplot(minutes,player1,player2,player3,labels=label,colors=color)
plt.legend(loc='upper left')
plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()
