import logging

import sys
from sqs_listener.daemon import Daemon
from sqs_listener import SqsListener
import httplib
import json

import pathos.multiprocessing as mp
#from multiprocessing.dummy import Pool as ThreadPool

class MyListener(SqsListener):
    def handle_message(self, body, attributes, messages_attributes):
        print(body['message'],body['mob_no'])
	"""
        post_data= json.dumps({"mnumber":body['mob_no'],"message": body['message'],"applicationId":10,"applicationKey":"asmaass"})    
        post_url='staging.clarifyd.in:8080'
        h = httplib.HTTPConnection(post_url)
        headers = {"Content-type": "application/json"}
        h.request('POST', '/notifier/api/rs/service/notify/sms', post_data, headers)
        r = h.getresponse()
        print(r)
        """
   
		

class MyDaemon(Daemon):
    def run(self,x):
        print ("Initializing listener ")
	listener = MyListener('sq', error_queue=None, region_name='ap-south-1')
        #listener.set_thread(x)
	listener.listen()
	

    def p(self):
    	pool = mp.Pool(2) #for process pool

    	pool.map(self.run,range(4))
    	print("done")
    #pool.join()


if __name__ == "__main__":
    daemon = MyDaemon('/var/run/sqs_daemon.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            print ("Starting listener daemon")
            daemon.p()
        elif 'stop' == sys.argv[1]:
            print ("Attempting to stop the daemon")
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print ("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print ("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)


logger = logging.getLogger('sqs_listener')
logger.setLevel(logging.INFO)

sh = logging.FileHandler('mylog.log')
sh.setLevel(logging.INFO)

formatstr = '[%(asctime)s - %(name)s - %(levelname)s]  %(message)s'
formatter = logging.Formatter(formatstr)

sh.setFormatter(formatter)
logger.addHandler(sh)
