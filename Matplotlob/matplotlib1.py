import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

""" Types of data

1)Categorical Data 
2)Numerical Data

"""
 #<------------------2d line plot----------------------->
""" Use for -
 1)bivariate analysis
 2)categorical & numerical or numerical & numerical
 3)Use cases- Time Series data
 """
# iphone_prices_inr = [41500, 50000, 58500, 63000, 67000, 84000, 92000, 100000, 108000, 116000]  
# iphone_years = [2007, 2008, 2010, 2012, 2014, 2017, 2018, 2019, 2020, 2023]  
# plt.plot(iphone_years,iphone_prices_inr)
# plt.show()
"""plot attribute
1)color
2)linewidth
3)marker-D,O,<,>,.
4)linestyle - solid,dashed,dot,dashdot
5)markersize
6)label
"""
batsman=pd.read_csv("Data-Visualization/Matplotlob/datasets/sharma-kohli.csv")
# print(batsman.head())
# plt.plot(batsman["index"],batsman['RG Sharma'],color="red",linewidth=3,marker="o",label="Rohit") #use hexcode to do apply any color
# plt.plot(batsman["index"],batsman['V Kohli'],color="blue",linewidth=3,marker="o",label="Virat")

# #title label 
# plt.title("Rohit Sharma VS Virat Kohli")
# plt.xlabel("Season")
# plt.ylabel("Runs Scored")
# plt.legend()
# #to tackle the outliers we can define the ylim,xlim
# plt.ylim(0,500)  only work in case of outliers
# plt.xlim(2008,2016)
# plt.grid()
# plt.show()

"""<------------------------Scatter plot----------------------->"""


# df=pd.read_csv("Data-Visualization/Matplotlob/datasets/batter.csv",nrows=50)
# plt.scatter(df['avg'],df["strike_rate"],color="red")
# plt.label("Avg and SR analysis of the batsman")
# plt.show()

# tips=sns.load_dataset('tips')
# # print(tips.head())
# plt.scatter(tips["total_bill"],tips['tip'],color="red",marker="D",s=tips["size"]*20)
# plt.show()

"""<------------Bar Chart-------------------->"""
children=list(np.random.randint(20,60,10))
colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Black", "White", "Cyan"]
# plt.bar(colors,children,color="red")
# plt.show()
#if number of categories is less at x-axis, use plt.bar() otherwise use plt.hbar()

df=pd.read_csv("Data-Visualization/Matplotlob/datasets/batsman_season_record.csv")
print(df.head())
# plt.bar(df["batsman"],df["2015"],width=0.1)
# plt.bar(np.arange(len(df))- 0.2,df["2015"],width=0.2,color="red")
# plt.bar(np.arange(len(df)),df["2016"],width=0.2,color='blue')
# plt.bar(np.arange(len(df))+ 0.2,df["2017"],width=0.2,color="green")
# plt.xticks(np.arange(len(df)),df["batsman"])
# plt.grid()
# plt.show()
# colors=[color*4 for color in colors]
# plt.bar(colors,children)
# # plt.xticks(rotation="vertical")
# plt.show()

"""<--------------stack bar chart----------->"""
# plt.bar(df['batsman'],df['2017'],label="2017")
# plt.bar(df['batsman'],df['2016'],bottom=df["2017"],label="2016")
# plt.bar(df['batsman'],df['2015'],bottom=df["2017"]+df["2016"],label="2015")
# plt.legend()
# plt.show()

"""<--------------histogram--------------------->"""
# usecase-->frequency counts
#use for univariate analysis
np.random.seed(54)
# data=np.random.randint(10,100,10)
# print(data)
# plt.hist(data)
# # plt.show()
df=pd.read_csv("Data-Visualization/Matplotlob/datasets/vk.csv")
plt.hist(df['batsman_runs'])
plt.show()