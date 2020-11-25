from django.apps import AppConfig
import os
import sys
import pandas as pd
from joblib import load

class PredictionConfig(AppConfig):
    name = 'Prediction'

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CLASSIFIER_FOLDER = os.path.join(BASE_DIR , 'Prediction/classifier/')
    CLSSIFIER_FILE =  os.path.join(CLASSIFIER_FOLDER , "IrisPrediction.joblib")
    classifier = load(CLSSIFIER_FILE)