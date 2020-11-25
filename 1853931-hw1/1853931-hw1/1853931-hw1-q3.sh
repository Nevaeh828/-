#!/bin/bash
file_name=$1
echo `cat ${file_name} | wc -l` >> 1853931-hw1-q3.log
echo `cat ${file_name} | wc -c` >> 1853931-hw1-q3.log
firstTime=`sed -n 1p ${file_name} | cut -d ' ' -f 2`
lastTime=`sed -n 100p ${file_name} | cut -d ' ' -f 2`
fTime=`date +%s -d $firstTime`
lTime=`date +%s -d $lastTime`
echo $fTime
echo $lTime
timeDiff=$(($lTime - $fTime))
echo $timeDiff >> 1853931-hw1-q3.log
times_sysloadin15=0
sum_sysloadin15=0
IFS="
"
for LINE in `cat ${file_name}`
do
	echo $LINE
	temp=`echo $LINE | cut -d ' ' -f 14`
	echo $temp
	if [ $temp != 0 ]
	then
		times_sysloadin15=$(($times_sysloadin15 + 1))
		sum_sysloadin15=$(echo "$sum_sysloadin15 + $temp"|bc)
	fi
done
ava_sysloadin15=$(echo "scale=4;$sum_sysloadin15 / $times_sysloadin15"|bc)
echo $times_sysloadin15
echo $ava_sysloadin15
#echo $ava_sysloadin15 >> 1853931-hw1-q3.log
if [ `echo "$ava_sysloadin15 >= 1"|bc` -eq 1 ]
then
    echo $ava_sysloadin15 >> 1853931-hw1-q3.log
else
    echo "0$ava_sysloadin15" >> 1853931-hw1-q3.log
fi
