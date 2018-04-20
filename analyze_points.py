import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import numpy as np
from itertools import cycle
import matplotlib.pyplot as plt
files=os.listdir(".")
#print(files)
colors = list('bgrcmybgrcmybgrcmybgrcmy')
for f in files:
	print(f)
	if f.startswith("Results"):
		print(f)
		fp=open(f,'r')
		xs=[]
		ys=[]
		X=[]
		for line in fp.readlines()[1:]:
			l=line.split(',')
			if float(l[1])<1500:continue
			x=float(l[5])
			y=float(l[6])
			X.append([x,y])
			xs.append(x)
			ys.append(y)
		#	print(x,y)
		if len(X)==0:continue
#		X = StandardScaler().fit_transform(X)
		X=np.array(X)
	#	print(X)

#		X=X.transpose()
		db = DBSCAN(eps=600, min_samples=10).fit(X)
		labels = db.labels_
		n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
		print('num',n_clusters_,labels)
		plt.title(f)
		col=[]
		for tt in range(len(labels)):
			if labels[tt]==-1:
				col.append('k')
			else:
				col.append(list(colors)[labels[tt]])
#		print(col)
		plt.scatter(xs, ys,color=col)
		#plt.scatter(xs, ys)
		plt.show()
		
