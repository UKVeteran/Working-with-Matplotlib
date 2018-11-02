import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



logins     = pd.read_csv('C:/Users/Johar/Desktop/Python - AI/Matplotlib/logins.csv',parse_dates=['Logged'])
grouped    = logins.groupby(by="Logged").sum()["Purchase"]


plt.plot(grouped.index, grouped.values,marker="D",linewidth=2.0,color="y")

plt.xlabel('Date')
plt.ylabel('Purchases')
plt.title('Purchases by Date')
plt.savefig("C:/Users/Johar/Desktop/Python - AI/Matplotlib/test.png")
plt.show()


#----------------------------------------------------------------#


grouped = grouped[grouped.index > "2008-07-07"]

plt.bar(grouped.index, grouped.values,width=1)
plt.xlabel('Date')
plt.ylabel('Purchases')
plt.title('Purchases by Date')
plt.grid(True)
plt.show()

#---------------------------------------------------------------#

ice_cream     = pd.read_csv('C:/Users/Johar/Desktop/Python - AI/Matplotlib/ice-creams.csv')

index = np.arange(ice_cream["Sales"].shape[0])

plt.bar(index, ice_cream["Sales"],width=0.5)
plt.xlabel('Type')
plt.ylabel('Sales')
plt.title('Sales by Ice Cream type')
plt.xticks(index + 1 / 4, ice_cream["Type"])
plt.show()

#---------------------------------------------------------------#

ice_cream     = pd.read_csv('C:/Users/Johar/Desktop/Python - AI/Matplotlib/stacked-ice-cream.csv')
ind = np.arange(4)
Vanilla   = ice_cream[ice_cream["Ice Cream Type"]=="Vanilla"]["Sales"]
Chocolate = ice_cream[ice_cream["Ice Cream Type"]=="Chocolate"]["Sales"]
Strawberry = ice_cream[ice_cream["Ice Cream Type"]=="Strawberry"]["Sales"]
Stores     = ice_cream.drop_duplicates("Store")["Store"]

p1 = plt.bar(ind, Vanilla,color="b",width=0.5)
p2 = plt.bar(ind, Chocolate,color="r",bottom=Vanilla,width=0.5)
p3 = plt.bar(ind, Strawberry,color="y",bottom=Vanilla,width=0.5)

plt.xticks(ind+0.25 , Stores)
plt.ylabel('Scores')
plt.title('Ice Cream Sales by Store Area')
plt.legend((p1[0], p2[0],p3[0]), ('Vanilla', 'Chocolate','Strawberry'))
plt.show()
