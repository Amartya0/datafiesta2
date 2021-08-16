import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy

'''
sd: 9,20        8,19
ib: 1,3
im: 5,1

'''

sd=pd.read_csv("./CorrectData/salesDetails_v1.csv")
ib=pd.read_csv("./CorrectData/itemBranch_v1.csv")
im=pd.read_csv("./CorrectData/itemMaster_v1.csv")

sd.columns = sd.columns.str.replace(' ','_')
ib.columns = ib.columns.str.replace(' ','_')
im.columns = im.columns.str.replace(' ','_')

#sd.info()
#ib.info()
#im.info()

itemSales = {}

imDict = {}

for i in range(im.shape[0]):
    if not math.isnan(im.iloc[i,5]):
        imDict[im.iloc[i,5]] = im.iloc[i,1]

ibDict = {}

for i in range(ib.shape[0]):
    if type(ib.iloc[i,1]) == str and not math.isnan(ib.iloc[i,3]):
        ibDict[ib.iloc[i,1]] = imDict[ib.iloc[i,3]]

def process(branchId, sales):
    if type(branchId) != str:
        return
    if math.isnan(sales):
        sales = 0
    try:
        itemSales[ibDict[branchId]] = itemSales[ibDict[branchId]] + sales
    except:
        try:
            itemSales[ibDict[branchId]] = sales
        except:
            pass

for i in range(sd.shape[0]):
    process(sd.iloc[i,8], sd.iloc[i,19])
    
final = {}

for i in sorted(itemSales.keys()):
    final[i] = itemSales[i]

itemSalesDF = pd.DataFrame(final.items())
itemSalesDF.info()
print(itemSalesDF)
itemSalesDF.plot(x=0,y=1,kind='bar')
plt.xlabel('Item Group')
plt.ylabel('Total Sales Amount')
plt.title('Total Sales Amount by Item Group')
plt.show()