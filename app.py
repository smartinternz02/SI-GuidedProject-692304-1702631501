import numpy as np
from flask import Flask, request, render_template,jsonify
import pickle
app=Flask(__name__)
model=pickle.load(open("training files\model.pkl",'rb'))
@app.route('/')
@app.route('/home',methods=['GET','POST'])
def home():
 return render_template('home.html')
@app.route('/about',methods=['GET','POST'])
def about():
 return render_template('about.html')
@app.route('/findingchurner',methods=['GET','POST'])
def findingchurner():
 return render_template('findingchurner.html')
@app.route('/predict', methods=['GET','POST'])
def predict():
 int_features = [int(x) for x in request.form.values()]
 features=[np.array(int_features)]
 prediction=model.predict(features)
 label_mapping = {0: 'low', 1: 'very low', 2: 'high', 3: 'very high'}
 predicted_label = label_mapping[prediction[0]]
 output = predicted_label
 return render_template('findingchurner.html',prediction_text='The chance of churn based on given customer info is {}'.format(output))
 #return jsonify(prediction_text = output)
if __name__=="__main__":
  app.run(debug=True)