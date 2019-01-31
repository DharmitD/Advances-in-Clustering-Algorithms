from pyclustering.cluster import cluster_visualizer;
from pyclustering.cluster.cure import cure;
import numpy as np
import pandas as  pd
import matplotlib.pyplot as plt

from pyclustering.utils import read_sample;
import timeit
from pyclustering.samples.definitions import FCPS_SAMPLES;

# Input data in following format [ [0.1, 0.5], [0.3, 0.1], ... ].
def cureAlgo(filename,col_name):
	df=pd.read_csv(filename, usecols=[col_name])
	df[col_name] = df[col_name]
	data = df[col_name]
	rownumber=len(data)
	if rownumber%2==1:
		rownumber+=1

	#converting pandas series into ndarray
	input_data=np.asarray(data)
	input_data.shape=(rownumber//2,2)
	print(input_data)
	print(input_data.shape)
	print("----------------------------------------------------------------------------------------------------------------------")
	# Allocate three clusters:
	cure_instance = cure(input_data.tolist(), 10);
	cure_instance.process();
	clusters = cure_instance.get_clusters();
	print(clusters)
	print(timeit.timeit('"-".join(str(n) for n in range(100))',number=10000))
	# Visualize clusters:
	visualizer = cluster_visualizer();
	visualizer.append_clusters(clusters, None);
	visualizer.show(display=False)
	plt.savefig("C:/Users/Nupura Hajare/Desktop/flask_app/web/static/img/CURE.png")
