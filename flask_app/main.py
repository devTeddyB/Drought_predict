from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
import jwt
import time


model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data_list = [[data1, data2, data3]]
    final = pd.DataFrame(data = data_list, columns=['stnNm','avgTa','sumRn'])
    pred = model.predict(final)

    def val(pred):
        if pred <= -2.0:
            return(f'심한 가뭄 : {pred}')
        elif pred > -2.0 and pred <= -1.5:
            return(f'보통 가뭄 : {pred}')
        elif pred > -1.5 and pred <= -1.0:
            return(f'약한 가뭄 : {pred}')
        elif pred > -1.0 and pred < 1.0:
            return(f'정상 : {pred}')
        else:
            return(f'습함 : {pred}')

    return render_template('pred.html', data1 = data1, fore=val(pred))



if __name__ == "__main__":
    app.run(debug=True)

