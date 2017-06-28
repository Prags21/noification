from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .launcher import launch
# Create your views here.
@csrf_exempt


def pub(request):
	if request.method == 'POST':
        	data = request.body.decode('utf-8')		
	i=json.loads(data)
	mesg=i['msg']   					#gives the message part
	id=i['me']						#id part
	launch(mesg,id)  					#launch function called for sending message to SQS 
        return HttpResponse("success")	

def fcm(request):
	


        return HttpResponse("success")	
