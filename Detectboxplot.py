import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
def outlierdetection(filename,col_name):
	df = pd.read_csv(filename)
	sns.boxplot(df[col_name])
	sns.despine()
	#fig = plt.figure(figsize=(7,4))
	#plt.scatter(data, clusters, alpha=1, edgecolor='black')
	plt.savefig("C:/Users/Nupura Hajare/Desktop/flask_app/web/static/img/outliers.png")
