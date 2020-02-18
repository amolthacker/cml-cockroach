import numpy as np
from sklearn.externals import joblib

# Load model

model = joblib.load('bikeshare_model.pkl')

# Function returns predicted rides given features

def predict_rides(args):
  features = np.array([args['season'],args['yr'],args['mnth'],args['holiday'],args['weekday'],args['workingday'],args['weathersit'],args['temp'],args['atemp'],args['hum'],args['windspeed']]).reshape(1, -1)
  return {'predicted_rides': int(model.predict(features)[0])}
