from django.shortcuts import render
from django.http import HttpResponse

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers_voice import serializers_voice_call_test
from .models import voice_call_array

import json
# Create your views here.
def index(request):
    return render(request,'index.html')
    
def call(request):
    return render(request,'call.html')
    
def receiver(request):
    return render(request,'receiver.html')
@api_view(['POST'])
def voice_call_post(request):
    voice_call_data=JSONParser().parse(request)
    file_name_json=voice_call_data['sender_number']
    #print("voice_call_data",voice_call_data)
    with open("json/"+str(file_name_json)+'.json', 'w') as json_file:
        json.dump(voice_call_data, json_file)
    #voice_call_post_serializer=serializers_voice_call_test(data=voice_call_data)
    #print("voice_call_post_serializer",voice_call_post_serializer.is_valid())
    #if voice_call_post_serializer.is_valid(raise_exception=True):
     #   voice_call_post_serializer.save()
    return JsonResponse(voice_call_data,status=status.HTTP_201_CREATED)
    #return JsonResponse(voice_call_post_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        
@api_view(['PUT'])
def voice_call_put(request,sender_number):
    try: 
        sender_number_id = voice_call_array.objects.get(sender_number=sender_number) 
    except voice_call_array.DoesNotExist: 
        return JsonResponse({'message': 'The voice_call_array does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    voice_call_data=JSONParser().parse(request)
    voice_call_put_serializer=serializers_voice_call_test(sender_number_id,data=voice_call_data)
    if voice_call_put_serializer.is_valid(): 
        voice_call_put_serializer.save() 
        return JsonResponse(voice_call_put_serializer.data) 
    return JsonResponse(voice_call_put_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET'])
def voice_call_get(request,sender_number):
    with open('json/'+str(sender_number)+'.json','r') as json_file:
        data=json.load(json_file)
        return JsonResponse(data) 
    
    #try: 
     #   sender_number_id = voice_call_array.objects.get(sender_number=sender_number) 
    #except voice_call_array.DoesNotExist: 
     #   return JsonResponse({'message': 'The voice_call_array does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    #voice_call_get_serializer = serializers_voice_call_test(sender_number_id) 
    #return JsonResponse(voice_call_get_serializer.data) 