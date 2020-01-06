#!/bin/bash
#a=$(date +%H:%M:%S)
#for i in `seq 1 10000`
#do
##curl -X GET   -H "Accept: text/xml" "http://mn01:20550/scanning_test100k/rk$i" >> tmp 2>&1 & 
#curl -X GET   -H "Accept: text/xml" "http://mn01:20550/scanning_test100k/rk$i" >> /dev/null 2>&1 & 
#done
#parallel -j 2 "curl -X GET -H \"Accept: text/xml\" \"http://mn01:20550/scanning_test100k/rk{}\" >> /dev/null 2>&1 &" ::: `seq 1 10000`
#wait
#parallel -j0 -N 252 --pipe "curl -X GET -s -H \"Accept: text/xml\" \"http://mn01:20550/scanning_test100k/rk{}\" >> tmp 2>&1 &" ::: `seq 1 10000`
#b=$(date +%H:%M:%S)

#echo -e "startTime:\t$a"
#echo -e "endTime:\t$b"
for i in `seq $1 $2`
do
#curl -X GET -s  -H "Accept: text/xml" "http://mn01:20550/scanning_test100k/rk$i" >> tmp 2>&1 & 
curl -X GET -s  -H "Accept: text/xml" "http://mn01:20550/scanning_test100k/rk$i" >> /dev/null 2>&1 & 
done
