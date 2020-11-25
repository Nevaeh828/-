#!/bin/bash
ssh root@101.132.134.84 -C "/bin/bash" < 1853931-hw1-q2.sh
ssh root@101.132.134.84 -C "/bin/bash" < 1853931-hw1-q3.sh >> 1853931-hw1-q2.log
scp root@101.132.134.84:/root/1853931-hw1-q3.log /home/apple/1.log
avg1=`sed -n 4p 1.log`
ssh root@47.101.213.235 -C "/bin/bash" < 1853931-hw1-q2.sh
ssh root@47.101.213.235 -C "/bin/bash" < 1853931-hw1-q3.sh >> 1853931-hw1-q2.log
scp root@47.101.213.235:/root/1853931-hw1-q3.log /home/apple/2.log
avg2=`sed -n 4p 2.log`
ssh root@47.101.220.165 -C "/bin/bash" < 1853931-hw1-q2.sh
ssh root@47.101.220.165 -C "/bin/bash" < 1853931-hw1-q3.sh >> 1853931-hw1-q2.log
scp root@47.101.213.235:/root/1853931-hw1-q3.log /home/apple/3.log
avg3=`sed -n 4p 3.log`
sum=$(echo "$avg1 + $avg2 + $avg3"|bc)
avg=$(echo "scale=4;$sum / 3"|bc)
if [ `echo "$avg >= 1"|bc` -eq 1 ]
then
    echo $avg >> 1853931-hw1-q4.log
else
    echo "0$avg" >> 1853931-hw1-q4.log
fi
