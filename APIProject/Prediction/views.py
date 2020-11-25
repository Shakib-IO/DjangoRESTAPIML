from django.shortcuts import render
from rest_framework import status

#The decorator converts a python function to an API function
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