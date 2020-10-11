#!/bin/bash
sum=0
for i in $(seq 2 100); do
  for j in $(seq 2 $i); do
    if [ $(( $i % $j )) -eq 0 ]; then
      break
    fi;
  done
 #echo "i:$i j:$j"
  if [ $i -eq $j ]; then
    sum=$(( $sum + $i ))
    #echo "sum:$sum"
  fi;
done
echo "0-100之间的所有质数之和为$sum">1853931-hw1-q1.log
