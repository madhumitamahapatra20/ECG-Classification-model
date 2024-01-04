from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open('ECG_Phase2_model_KNN.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    coordinate = request.form.get('coordinate')
    coordinates=[]
    for i in coordinate.split():
        i=int(i)
        coordinates.append(i)
    arr1 = np.array(coordinates)
    print(arr1)
    minimum = arr1.min()
    prr1 = arr1 - minimum
    maximum = prr1.max()
    prr1 = prr1 / maximum
    result = model.predict([prr1])[0]

    if result==1:
        result = 'Abnormal'
    else:
        result = 'Normal'

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)