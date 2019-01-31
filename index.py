from flask import Flask,render_template,request,send_from_directory
from werkzeug import secure_filename
import pandas as pd
import numpy as np
from Writefile import processCsv
from algorithms.Kmode import kmode
from algorithms.Birch import birchAlgo
from algorithms.CURE import cureAlgo
from algorithms.Roc import rocAlgo
from Detectboxplot import outlierdetection
app = Flask(__name__,static_url_path='',static_folder='web/static',template_folder='web/templates')

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/uploadfile')
def uploadFile():
   return render_template('upload.html')

@app.route('/processFile',methods=['GET','POST'])
def processFile():
	if request.method == 'POST':
		file=request.files['dataset1']
		colname=request.form['colname']
		file.save(secure_filename(file.filename))
		data=processCsv(file.filename,colname)
		data.to_csv('./cleanedData/Result.csv')
		sampleData=list(data[colname][0:5])
		return render_template("upload.html",filename="Result.csv",sampleData=sampleData,colname=colname)

#@app.route('/outlierdetection',methods=['GET','POST'])
#def outlierdetection():
#	file=request.args.get('file')
#	colname=request.args.get('column')
#	df=pd.DataFrame()
#	filepath='./cleanedData/%s' % file
#	outlierdetection(filepath,colname)
#	return render_template('Detectoutliers.html')

		

@app.route('/get_cleanedfile/<filename>')
def get_cleanedfile(filename):
	return send_from_directory('cleanedData', filename)

@app.route('/applyAlorithm',methods=['GET','POST'])
def applyAlorithm():
	file=request.args.get('file')
	colname=request.args.get('column')
	df=pd.DataFrame()
	filepath='./cleanedData/%s' % file
	df=pd.read_csv(filepath)	
	rocAlgo(filepath,colname)
	kmode(filepath,colname)
	if df[colname].dtype.kind in 'if':
			outlierdetection(filepath,colname)
			cureAlgo(filepath,colname)
			birchAlgo(filepath,colname)
			return render_template('result.html',error_message=True)
	return render_template('result.html',error_message=False)



if __name__ == '__main__':
   app.run()
