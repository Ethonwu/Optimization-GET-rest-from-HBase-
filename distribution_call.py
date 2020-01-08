import os
import sys

key_num = int(sys.argv[1])
work_node = 6
worker_list = ['en01','mn01','mn02','wh01','wh02','wh03']
j = 0
for i in range(1,key_num,key_num/work_node):
    start_key = i 
    end_key = start_key + key_num/work_node
    command = 'ssh root@{} "python2.7 /root/mutithread_query_script/concurrent_processing.py {} {} "'.format(worker_list[j],start_key,end_key)
    print command
    os.system(command)
    j = j + 1 
