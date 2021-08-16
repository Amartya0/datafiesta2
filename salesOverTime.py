import pandas as pd
import matplotlib.pyplot as plt
import math

sd=pd.read_csv("./CorrectData/salesDetails_v1.csv")
sd.columns = sd.columns.str.replace(' ','_')

avgs = {}
processed = {}

def date2int(date):
    if type(date) == float: return 0
    
    d, m, y = list(map(int, date.split("/")))
    inc = 0
    m = m if m < 13 else d
    
    if m < 4:
        inc = 0
    elif m < 7:
        inc = 0.25
    elif m < 10:
        inc = 0.5
    else:
        inc = 0.75
    return y + inc

def avgDict(date, sales):
    if math.isnan(sales) and date != 0:

        sales = 0

    try:
        avgs[date] = avgs[date] + sales
    except:
        avgs[date] = sales
    
for i in range(sd.shape[0]): 
    if sd.iloc[i,6] != None: 
        avgDict(date2int(sd.iloc[i,6]), sd.iloc[i,19])

    
print(avgs)

for i in sorted(list(avgs.keys())):
    if i != 0:
        if avgs[i] == None:
            processed[i] = 0
        else:
            processed[i] = avgs[i]
    
test = pd.DataFrame(processed.items())

test.plot(x=0, y=1, kind='line')
plt.xlabel("year")
plt.ylabel("Total sales ammount")
plt.title("Total sales ammount over time")
plt.show()
