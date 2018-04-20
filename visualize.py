import numpy as np 
from sklearn.metrics import *

import matplotlib.pyplot as plt
stat=[]
fp=open('Steatosis_stage(public).csv')
for line in fp.readlines()[1:-1]:
    print(line.split(','))
    idd,stage,count,total_area,slice_area,nn,ratio,_,_,_=line.split(',')
    stat.append([idd,int(stage),count,float(total_area),float(slice_area),nn,float(ratio)])
#print stat
box_data=[0,0,0]
count_data=[0,0,0]
plot_data=[[],[],[]]
plot_data_count=[[],[],[]]
for i in stat:
    box_data[i[1]-1]+=i[-1]
    count_data[i[1]-1]+=1
    print(i[-1])
    plot_data[i[1]-1].append(i[-1])
    plot_data_count[i[1]-1].append(i[-2])

for i in range(len(box_data)):
    box_data[i]/=count_data[i]
#plt.bar([1,2,3],box_data)
'''
plt.plot(plot_data[0],color='blue',label='1',marker='o')
plt.plot(plot_data[1],color='yellow',label='2',marker='o')
plt.plot(plot_data[2],color='red',label='3',marker='o')
'''
plt.scatter(plot_data[0],plot_data_count[0],color='blue',label='1',marker='o')
plt.scatter(plot_data[1],plot_data_count[1],color='yellow',label='2',marker='o')
plt.scatter(plot_data[2],plot_data_count[2],color='red',label='3',marker='o')
plt.legend()
plt.show()





