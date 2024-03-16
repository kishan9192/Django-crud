from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view

# creating a request to playground/hello

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello world')


@api_view(['GET', 'POST'])
def drink_list(request):
    
    if request.method == 'GET':
        #get all drinks
        #serialize them
        #return JSON

        drinks = Drink.objects.all()
        
        #many=True means serialize all the objects
        serializer =  DrinkSerializer(drinks, many=True)

        return JsonResponse({"drinks": serializer.data})
    
    if request.method == 'POST':
       serializer = DrinkSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_detail(request, id):

    try:
        # get the drink from the drinks object whose primary key (pk) matches the drink id passed in params
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
         serializer = DrinkSerializer(drink)
         return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
