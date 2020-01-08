#!/usr/bin/env python

import concurrent.futures
import time
import sys,os
import urllib2
#import requests
#from requests import async


  

def millis():
  return int(round(time.time() * 1000))

def http_get(url):
  #start_time = millis()
  opener = urllib2.build_opener()
  opener.addheaders = [('Accept',' text/xml')]
#
#  #urllib2.addheaders = [('Accept',' text/xml')]
  #res = opener.open(url)
  opener.open(url)
#  
  #print res.read()
  #return res
#def http_get(url):
#    r = requests.get(url, headers ={'Accept': 'text/xml'})
#    print r.text
    #async.get(url, headers ={'Accept': 'text/xml'})
def scrap():
    with concurrent.futures.ProcessPoolExecutor(max_workers=20) as executor:
    #with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        #future_to_url = {executor.submit(http_request, url): url for url in urls}
	results = executor.map(http_get, urls)
        #for future in concurrent.futures.as_completed(future_to_url):
            #url = future_to_url[future]
            #try:
                #data = future.result()
            #except Execption as exc:
                #print('%r generated an exception: %s' % (url, exc))
           # else:
		#print('%r page length is %d' % (url, len(data)))
#query_num = 10000
#query_num = 200
#sample_mn01 = "http://www.google.com"
#sample_mn01 = "http://en01"
sample_wh01 = "http:/mn01:20550/scanning_test100k/rk1"
#sample_wh01 = "http://wh01:20550/scanning_test100k/rk"
#p_num = int(sys.argv[1])
global urls
start_key = int(sys.argv[1])
end_key = int(sys.argv[2])

urls = []
for i in range(start_key,end_key):
   #urls.append(sample_mn01+str(i))  
   urls.append(sample_mn01)  
#for i in range(query_num/2+1,query_num+1):
#   urls.append(sample_wh01+str(i))

start_time = millis()
scrap()
total_time = str(millis() - start_time)
print "Total took {} ms".format(total_time)
#for result in results:
#  print result
#command = "hostname > time.txt ;  echo -e '\nTotal took {} ms\n' >> time.txt".format(total_time)
#os.system(command)
