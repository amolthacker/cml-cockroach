import numpy as np
from sklearn.externals import joblib
import logging
import logging.handlers

logger = logging.getLogger('Ifi.Log')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter("%(asctime)s\t%(process)d\t%(levelname)s\t%(name)s\t%(message)s"))
logging.getLogger().addHandler(handler)


# Load model

print("IFI:loading model")
logger.info('IFI:loading model')
logger.debug('IFI:loading model')

model = joblib.load('bikeshare_model.pkl')

# Function returns predicted rides given features

def predict_rides(args):
  print("IFI: extracting features")
  logger.info("IFI-info: extracting features")
  logger.debug("IFI-debug: extracting features")
  features = np.array([args['season'],args['yr'],args['mnth'],args['holiday'],args['weekday'],args['workingday'],args['weathersit'],args['temp'],args['atemp'],args['hum'],args['windspeed']]).reshape(1, -1)
  print("IFI: returning prediction")
  logger.info("IFI-info: returning prediction")
  logger.debug("IFI-debug: returning prediction")
  return {'predicted_rides': int(model.predict(features)[0])}

print("IFI:bye!")
logger.info('IFI:bye!')
logger.debug('IFI:bye!')

predict_rides({
  "season": 3,
  "yr": 1,
  "mnth": 8,
  "holiday": 0,
  "weekday": 3,
  "workingday": 1,
  "weathersit": 1,
  "temp": 0.7175,
  "atemp": 0.667308,
  "hum": 0.6775,
  "windspeed": 0.141179
})
