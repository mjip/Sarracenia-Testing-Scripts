#!/bin/bash

# don't run this file it'll eat all your memory

STN_ID_ARR=()
for c1 in $(seq -f "%02g" 0 99)
do
	for c3 in {A..K}
	do
		for c4 in {A..K}
		do
			for c5 in $(seq -f "%03g" 0 999)
			do
				STN_ID_ARR+=($c1$c3$c4$c5)
			done
		done
	done
done
printf '%s\n' "${STN_ID_ARR[@]}"
for stn_id in ${#STN_ID_ARR[@]}
do
	response=`curl -I http://environment.alberta.ca/apps/Basins/data/figures/river/abrivers/stationdata/"$STN_ID"_table.json | head -n 1`

	response_arr=($response)

	echo ${response_arr[1]}
done
