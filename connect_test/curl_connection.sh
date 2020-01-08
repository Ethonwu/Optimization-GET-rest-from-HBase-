#!/bin/bash
#a=$(date +%H:%M:%S)
for i in `seq 0 $1`
do
  curl http://en01 > /dev/null 2>&1 &
done
#b=$(date +%H:%M:%S)
#echo -e "startTime:\t$a"
#echo -e "endTime:\t$b"
