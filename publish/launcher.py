from sqs_launcher import SqsLauncher
import sys
import json
from .dao import fetch
result=[]
def launch(message,p_id):			#sends message to the queue
        launcher = SqsLauncher('sq')
	#print(message)
	#assign mobile numbers to var mob for a given parent id  
	mob=fetch(p_id)
	for m in mob:
		print(m[0])
    		r=launcher.launch_message({'message': message, 'mob_no': m[0]})
		#print(r)