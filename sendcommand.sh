#!/bin/bash
filename=$1
commands=$2
if [ -z "$1" ] || [ -z "$2" ]
then
  echo '$1 or $2 is empty'
  exit 0
else
    for i in `cat $1`
    do
        #echo "Now Doing $i user and command is $command"
        ssh root@$i "$commands"
    done
fi
