#!/usr/bin/env bash

path="https://zenodo.org/record/1188976/files"
request="download=1"
destination= "videos"

mkdir -p "${destination}"

for i in  0{1..9} {10..15}
do
	filename="Video_Song_Actor_${i}.zip"
    full_path="${path}/${filename}?${request}"
    wget "${full_path}" -O "${destination}/${filename}"
done
