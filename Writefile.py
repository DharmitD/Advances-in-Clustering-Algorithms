import numpy as np
import pandas as  pd
import csv

def processCsv(filename,colname):
	df=pd.read_csv(filename)
	for col in df:
		#print(col)
		#print(df[col].dtype.kind)
		if df[col].dtype.kind in 'if':	
			df[col]=df[col].fillna(df[col].mean())
		else:
			df[col]=df[col].fillna("?")
	return df






#integer and float 'if'
#if df[colname].dtype==np.number:
		#df[colname]=df[colname].replace('?',df[colname].mean())

#processCsv('Product.csv','')