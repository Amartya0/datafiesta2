import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy

'''
sd: 2, 20 1,19
cs: 2, 4
rg: 1, 0

'''

sd=pd.read_csv("./CorrectData/salesDetails_v1.csv") 
rg=pd.read_csv("./CorrectData/region_v1.csv")
cs=pd.read_csv("./CorrectData/customers_v1.csv")
sd.columns = sd.columns.str.replace(' ','_')
rg.columns = rg.columns.str.replace(' ','_')
cs.columns = cs.columns.str.replace(' ','_')
# sd.info()
# cs.info()
# rg.info()
custDict = {}
regDict = {}

for i in range(rg.shape[0]):
    if type(rg.iloc[i,1]) == numpy.int64:
        regDict[rg.iloc[i,1]] = rg.iloc[i,0]    
         

for i in range(cs.shape[0]):
    if type(cs.iloc[i,2]) == numpy.int64:
        try:
            custDict[cs.iloc[i,2]] = regDict[cs.iloc[i,4]]
        except:
            pass   

regionalSales = {}

def process(custId, sales):
    if type(custId) != numpy.int64: return    
    if math.isnan(sales):
        sales = 0
    
    try:
        regionalSales[custDict[custId]] = regionalSales[custDict[custId]] + sales
    except:
        regionalSales[custDict[custId]] =sales

for i in range(sd.shape[0]):
    process(sd.iloc[i,1], sd.iloc[i,19])
    
    
rgSales = pd.DataFrame(regionalSales.items())
rgSales.plot(x=0,y=1,kind='bar')
plt.ylabel('Total Sales Amount')
plt.xlabel('Region')
plt.title('Sales by Region')
plt.show()