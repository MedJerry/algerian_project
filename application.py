from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
import sklearn.preprocessing as standarscaler
from flask import Flask,request,jsonify,render_template

application = Flask(__name__)
app = application


##import ridge regressor and standard scaler pickle
ridge_model = pickle.load(open('model/ridgecv.pkl', 'rb'))
standard_scaler = pickle.load(open('model/scaler.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('home.py')
@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoints():
    if request.method == 'POST':
        Temperature = float(request.form['Temperature'])
        RH = float(request.form['RH'])
        Ws = float(request.form['Ws'])
        Rain = float(request.form['Rain'])
        FFMC = float(request.form['FFMC'])
        DMC = float(request.form['DMC'])
        ISI = float(request.form['ISI'])
        Classes = float(request.form['Classes'])
        Region = float(request.form['Region']) 

        new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_data_scaled)
        return render_template('home.html', result=result[0])

    else:
        return render_template('index.py')
if __name__ == '__main__':
    app.run(host='0.0.0.0') 
