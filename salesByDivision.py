import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy

'''
sd: 2,20        1,19
cs: 2,3
dv: 1,0

'''

sd=pd.read_csv("./CorrectData/salesDetails_v1.csv")
#sd=pd.read_csv("./temp.csv") 
cs=pd.read_csv("./CorrectData/customers_v1.csv")
dv=pd.read_csv("./CorrectData/division_v1.csv")

sd.columns = sd.columns.str.replace(' ','_')
cs.columns = cs.columns.str.replace(' ','_')
dv.columns = dv.columns.str.replace(' ','_')

#sd.info()
#cs.info()
#dv.info()

divDict = {}

for i in range(dv.shape[0]):
    if not math.isnan(dv.iloc[i,1]):
        divDict[dv.iloc[i,1]] = dv.iloc[i,0]
        
csDict = {}

for i in range(cs.shape[0]):
    if not math.isnan(cs.iloc[i,2]) and not math.isnan(cs.iloc[i,3]):
        try:
            csDict[cs.iloc[i,2]] = divDict[cs.iloc[i,3]]
        except:
            pass
        
divSales = {}
def process(custKey, sales):
    if math.isnan(custKey):
        return
    if math.isnan(sales):
        sales = 0
    try:
        divSales[csDict[custKey]] = divSales[csDict[custKey]] + sales
    except:
        try:
            divSales[csDict[custKey]] = sales
        except:
            pass

for i in range(sd.shape[0]):
    process(sd.iloc[i,1], sd.iloc[i,19])
    
final = []

keys = list(divSales.keys())
for i in range(len(keys)):
    final.append([i, keys[i], divSales[keys[i]]])

divSalesDF = pd.DataFrame(final)

divSalesDF.plot(x=1 , y=2, kind='bar')
plt.xlabel('Division')
plt.ylabel('Total Sales amount')
plt.title('Total Sales by Division')
plt.show()