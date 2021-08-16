import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy

'''
sd: 2,20        1,19
cs: 2,0
ca: 0,2

'''

sd=pd.read_csv("./CorrectData/salesDetails_v1.csv")
#sd=pd.read_csv("./temp.csv") 
cs=pd.read_csv("./CorrectData/customers_v1.csv")
ca=pd.read_csv("./CorrectData/customerAddress_v1.csv")

sd.columns = sd.columns.str.replace(' ','_')
cs.columns = cs.columns.str.replace(' ','_')
ca.columns = ca.columns.str.replace(' ','_')

#sd.info()
#cs.info()
#ca.info()

caDict = {}

for i in range(ca.shape[0]):
    if not math.isnan(ca.iloc[i,0]):
        caDict[ca.iloc[i,0]] = ca.iloc[i,2]
        
csDict = {}

for i in range(cs.shape[0]):
    if not math.isnan(cs.iloc[i,2]) and not math.isnan(cs.iloc[i,0]):
        try:
            csDict[cs.iloc[i,2]] = caDict[cs.iloc[i,0]]
        except:
            pass

countrySales = {}

def process(custKey, sales):
    if math.isnan(custKey):
        return
    if math.isnan(sales):
        sales = 0
        
    try:
        countrySales[csDict[custKey]] = countrySales[csDict[custKey]] + sales
    except:
        try:
            countrySales[csDict[custKey]] = sales
        except:
            pass

for i in range(sd.shape[0]):
    process(sd.iloc[i,1], sd.iloc[i,19])        

final = []
keys = list(countrySales.keys())

for i in range(len(keys)):
    final.append([i, keys[i], countrySales[keys[i]]])
    
countrySalesDF = pd.DataFrame(final)
countrySalesDF.plot(x=1 , y=2, kind='bar')
plt.xlabel('Country')
plt.ylabel('Total Sales amount')
plt.title('Total Sales by Country')
plt.show()
