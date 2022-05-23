#from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt # enable other domains to access our API methods
from rest_framework.parsers import JSONParser # parse the incoming data to data model
from django.http.response import JsonResponse

from .models import Hero
from .serializers import HeroSerializer

@csrf_exempt
def heroApi(request, id=0):
    if request.method =='GET':
        heroes = Hero.objects.all()
        heroes_serializer = HeroSerializer(heroes, many=True) #convert to JSON format 
        return JsonResponse(heroes_serializer.data, safe=False)
    elif request.method =='POST': #insert record
        hero_data = JSONParser().parse(request) #request parsed
        heroes_serializer = HeroSerializer(data=hero_data) #convert request to model
        if heroes_serializer.is_valid():
            heroes_serializer.save()
            return JsonResponse("Added Succesfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT': #update record 
        hero_data = JSONParser().parse(request) #request parsed
        hero = Hero.objects.get(heroId=hero_data['heroId']) #capture existing data using heroId
        heroes_serializer = HeroSerializer(hero, data=hero_data) #map the new values
        if heroes_serializer.is_valid():
            heroes_serializer.save()
            return JsonResponse("Updated Succesfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        hero = Hero.objects.get(herId=id)
        hero.delete()   
        return JsonResponse("Deleted Successfully", safe=False)