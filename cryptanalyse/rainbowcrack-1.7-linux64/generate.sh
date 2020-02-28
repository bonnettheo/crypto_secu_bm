#!/bin/bash

#generate lm
#for i in 7
#do
#	for typo in "loweralpha" "mixalpha" "ascii-32-95"
#	do
#		./rtgen lm $typo 1 $i 0 100000 100000 0
#		./rtsort lm_${typo}#1-${i}_0_100000x100000_0.rt
#		echo "done ${typo} ${i}"
#	done
#done

#generate ntlm
#for i in 5 10 15
#do
#	for typo in "loweralpha" "mixalpha" "ascii-32-95"
#	do
#		./ntlm md5 $typo 1 $i 0 100000 100000 0
#		./ntlm md5_${typo}#1-${i}_0_100000x100000_0.rt
#		echo "done ${typo} ${i}"
#	done
#done

#generate md5
#for i in 5 10 15
#do
#	for typo in "loweralpha" "mixalpha" "ascii-32-95"
#	do
#		./rtgen md5 $typo 1 $i 0 100000 100000 0
#		./rtsort md5_${typo}#1-${i}_0_100000x100000_0.rt
#		echo "done ${typo} ${i}"
#	done
#done

#generate sha1
for i in 15 20
do
	for typo in "loweralpha" "mixalpha" "ascii-32-95"
	do
		./rtgen sha1 $typo 1 $i 0 100000 100000 0
		./rtsort sha1_${typo}#1-${i}_0_100000x100000_0.rt
		echo "done ${typo} ${i}"
	done
done

#generate sha256
for i in 5 10 15 20
do
	for typo in "loweralpha" "mixalpha" "ascii-32-95"
	do
		./rtgen sha256 $typo 1 $i 0 100000 100000 0
		./rtsort sha256_${typo}#1-${i}_0_100000x100000_0.rt
		echo "done ${typo} ${i}"
	done
done

