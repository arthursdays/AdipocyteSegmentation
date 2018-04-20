import numpy as np 
from sklearn.metrics import *
fp=open('Steatosis_stage(public).csv')
stat=[]
for line in fp.readlines()[1:-1]:
    idd,stage,count,total_area,slice_area,nn,ratio=line.split(',')
    stat.append([idd,int(stage),count,float(total_area),float(slice_area),nn,float(ratio)])


def predict(v):
#    return 1
    if v>7.0 and v<12:
        return 2
    elif v>12.0:
        return 3
    else:
        return 1

def evaluate_error(data,stages):
    predict_labels=[predict(x) for x in data]
    accuracy = 1-zero_one_loss(predict_labels, stages)
    print (accuracy)
evaluate_error([x[-1] for x in stat],[x[1] for x in stat])



