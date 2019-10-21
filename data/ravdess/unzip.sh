#!/usr/bin/env bash

apt-get install unzip

destination="videos"

cd "./${destination}"
echo "${pwd}"

for i in  0{1..9} {10..15}
do
	filename="Video_Song_Actor_${i}.zip" 
	echo "${filename}"
    unzip "${filename}"
    rm "${filename}"
done