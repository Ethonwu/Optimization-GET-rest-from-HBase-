# coding=utf-8
import threading
import sys
import os
import time


def job():
    #command = "sh ./get_query.sh {} {}".format(row_range,end_range)
    #print command
    os.system("sh ./range_query.sh {} {}".format(row_range,end_range))
    time.sleep(1) 
    #print query_result
    # print(query_str)


if __name__ == "__main__":
    threads = []
    thread_num = int(sys.argv[1])
    query_rows = 10000
    #i = thread_num
    #i = 1
    i = 0
    global row_range,end_range
    for row_range in range(1,query_rows,query_rows/thread_num):
	end_range = row_range+query_rows/thread_num
	threads.append(threading.Thread(target=job))
	threads[i].start()
	i = i + 1
    for j in range(thread_num):
        threads[j].join()
    #sys.exit(0)
    #for i in range(thread_num):
    #    threads.append(threading.Thread(target=job))
    #    threads[i].start()

    #for i in range(thread_num):
    #    threads[i].join()

