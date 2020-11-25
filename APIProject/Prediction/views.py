from django.shortcuts import render

#Create API with API View Function 
from rest_framework import status
##The decorator converts a python function to an API function
from rest_framework.decorators import api_view 
from rest_framework.response import Response

# Create your views here.
@api_view(['GET' , 'POSt'])
def api_add(request):
    sum = 0
    response_dict = {}
    if request.method =="GET":
        pass
    elif request.method == "POST":
        data =  request.data
        for key in data:
            sum += data[key]
        response_dict = {"sum ": sum}
    return Response(response_dict , status=status.HTTP_201_CREATED)


#Create API with Class Based Views
from rest_framework.views import APIView

class Add_values(APIView):
    def post(self , request, format = None):
        sum = 0
        data = request.data
        for key in data:
            sum += data[key]
        response_dict = {"sum" : sum}
        return Response(response_dict , status=status.HTTP_201_CREATED)

# Class based view to predict based on IRIS model
from .apps import PredictionConfig
import pandas as pd 

class IRIS_Model_Predict(APIView): 
    def post(self , request , format = None):
        data = request.data 
        keys = []
        values = []
        for key in data:
            keys.append(key)
            values.append(data[key])
        
        X = pd.Series(values).to_numpy().reshape(1 ,-1)
        loaded_classifier = PredictionConfig.classifier
        y_pred = loaded_classifier.predict(X)
        y_pred =  pd.Series(y_pred)
        target_map = {0: 'setosa' , 1: 'versicolor' , 2:'virginica'}
        y_pred =  y_pred.map(target_map).to_numpy()
        response_dict = {"Prediced Iris Species": y_pred[0]}
        return Response(response_dict, status=200)