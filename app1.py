from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# create an instance
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Set the URL for the Function
@app.route('/output' , methods = ["POST"])
def TOP10():
    if request.method == 'POST':
        name = request.form['name']
        sleep = request.form['sleep']

        regressor = pickle.load(open('new_model.pkl', 'rb'))

        input = np.array(float(sleep)).reshape(-1,1)
        output = round(regressor.predict(input)[0][0],2)

        hours,min = str(output).split('.')
        if int(min[0])>6: return render_template('success.html', n = name,o = float(sleep) ,h = int(hours)+1)
        return render_template('success.html', n = name,o = float(sleep) ,h = int(hours))


if __name__ == '__main__':
    app.run(debug=True)
