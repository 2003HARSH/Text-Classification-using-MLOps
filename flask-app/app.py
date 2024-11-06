from flask import Flask, render_template, request
import mlflow, dagshub
from preprocessing_utility import normalize_text
import pickle

#load model from mlflow
mlflow.set_tracking_uri('https://dagshub.com/2003HARSH/Text-Classification-using-MLOps.mlflow')

dagshub.init(repo_owner='2003HARSH', repo_name='Text-Classification-using-MLOps', mlflow=True)

model_name='my_model'
model_version=2

model_uri=f'models:/{model_name}/{model_version}'

model=mlflow.pyfunc.load_model(model_uri)

#load vectorizer BOW
vectorizer=pickle.load(open('models/vectorizer.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',result=None)

@app.route('/predict',methods=['POST'])
def predict():
    text=request.form['text']
    
    #clean text
    text=normalize_text(text)

    #BOW
    features=vectorizer.transform([text])

    #predict
    result=model.predict(features)

    return render_template('index.html',result=result[0])


app.run(debug=True)