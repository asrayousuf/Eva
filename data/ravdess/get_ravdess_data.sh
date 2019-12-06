#!/bin/bash

path="https://zenodo.org/record/1188976/files"
request="download=1"
destination="videos"

mkdir -p "${destination}"

for i in  0{1..9} {10..24}
do
    filename="Video_Speech_Actor_${i}.zip"
    full_path="${path}/${filename}?${request}"
    wget -O "${destination}/${filename}" "${full_path}"

    unzip "${destination}/${filename}" -d "${destination}"
    rm "${destination}/${filename}"
done

for i in  0{1..9} {10..24}
do
    folder="videos/Actor_${i}"
    mv ${folder}/* "videos/"
    rm -rf ${folder}
done

mkdir -p "videos/01.neutral"
mkdir -p "videos/02.calm"
mkdir -p "videos/03.happy"
mkdir -p "videos/04.sad"
mkdir -p "videos/05.angry"
mkdir -p "videos/06.fearful"
mkdir -p "videos/07.disgust"
mkdir -p "videos/08.surprised"

python classify_data.py
python extract_better_frames.py

echo "--------Finished processing RAVDESS--------"
