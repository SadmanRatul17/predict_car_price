

import numpy as np
from flask import Flask,render_template,request
import pandas as pd
import pickle
app = Flask(__name__)

model = pickle.load(open("LinearRegressionModel.pkl",'rb'))
df = pd.read_csv("cleaned car.csv")

@app.route('/')

def index():

    companies = sorted(df['company'].unique())
    car_model = sorted(df['name'].unique())
    year = sorted(df['year'].unique(), reverse=True)
    fuel_type = df['fuel_type'].unique()
    return render_template('index.html',companies=companies,  car_model =car_model, years = year, fuel_types =fuel_type )

@app.route('/predict', methods=['POST'])
def predict():

    company = request.form.get('company')
    car_model = request.form.get('car_models')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))


    prediction = model.predict(pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]],columns=['name','company','year','kms_driven','fuel_type']))


    return str(np.round(prediction[0],2))

if __name__ == "__main__" :
    app.run(debug=True)