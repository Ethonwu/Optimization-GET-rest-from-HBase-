#!/usr/bin/env python

from multiprocessing import Process, Pool
import time
import sys
import urllib2

def millis():
  return int(round(time.time() * 1000))

def http_get(url):
  start_time = millis()
  opener = urllib2.build_opener()
  opener.addheaders = [('Accept',' text/xml')]
  res = opener.open(url).read()
  print "\nTotal took " + str(millis() - start_time) + " ms\n"
  #time.sleep(1)
  return res
  
#urls = ['http://www.google.com/', 'https://foursquare.com/', 'http://www.yahoo.com/', 'http://www.bing.com/', "https://www.yelp.com/"]
query_num = 10000
sample_mn01 = "http://mn01:20550/scanning_test100k/rk"
sample_wh01 = "http://wh01:20550/scanning_test100k/rk"
p_num = int(sys.argv[1])
urls = []
for i in range(1,query_num+1):
   urls.append(sample_mn01+str(i))  
#for i in range(query_num/2+1,query_num+1):
#   urls.append(sample_wh01+str(i))
pool = Pool(processes=p_num)

start_time = millis()
results = pool.map(http_get, urls)
total_time = str(millis() - start_time)

#for result in results:
#  print result
print "\nTotal took " + total_time + " ms\n"
  
