#!/bin/bash
num=0
while true
do
uptime >> 1853931-hw1-q2.log
num=$(($num + 1))
echo "$num"
if [ $num -ge 100 ]; then break; fi
sleep 10
done

