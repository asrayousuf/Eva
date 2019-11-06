import os
import shutil

mapping = {
    '01': '01.neutral',
    '02': '02.calm',
    '03': '03.happy',
    '04': '04.sad',
    '05': '05.angry',
    '06': '06.fearful',
    '07': '07.disgust',
    '08': '08.surprised'
}

for filename in os.listdir('.'):
    if filename.endswith('.mp4'):
        file_arr = filename.split('-')
        emotion_tag = file_arr[2]
        shutil.move(filename, mapping[emotion_tag])
