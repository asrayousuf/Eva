#!/usr/bin/env bash

for i in 0{1..9} {10..24}
do
	filename="Video_Speech_Actor_${i}.zip"
    unzip "${filename}"
    rm "${filename}"
done
