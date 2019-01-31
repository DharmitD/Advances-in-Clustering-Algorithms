# an example of clustering by BIRCH algorithm.
from pyclustering.cluster.birch import birch;
import numpy as np
import pandas as  pd
import csv
from pyclustering.cluster import cluster_visualizer;
import matplotlib.pyplot as plt
from pyclustering.utils import read_sample
import timeit
from pyclustering.samples.definitions import FCPS_SAMPLES;

from pyclustering.utils import read_sample;


def birchAlgo(filename,col_name):
		df=pd.read_csv(filename, usecols=[col_name])
		df[col_name] = df[col_name]
		data = df[col_name]
		rownumber=len(data)
		if rownumber%2==1:
			rownumber+=1

		#converting pandas series into ndarray
		input_data=np.asarray(data)
		input_data.shape=(rownumber//2,2)
		print(input_data.dtype)
		print(input_data.shape)
		print("----------------------------------------------------------------------------------------------------------------------")
		# create BIRCH algorithm for allocation three objects.
		birch_instance = birch(input_data.tolist(), 10)
		# start processing - cluster analysis of the input data.
		birch_instance.process()
		# allocate clusters.
		clusters = birch_instance.get_clusters();
		print(clusters)
		print(timeit.timeit('"-".join(str(n) for n in range(100))',number=10000))
		#Visualize clusters:
		visualizer = cluster_visualizer()
		visualizer.append_clusters(clusters,input_data)
		visualizer.show(display=False)
		plt.savefig("C:/Users/Nupura Hajare/Desktop/flask_app/web/static/img/birch.png")
