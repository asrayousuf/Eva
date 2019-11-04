import os
from PIL import Image
import face_recognition
import json

def getBoundingBox(img_path):
    image = face_recognition.load_image_file(img_path)
    face_location = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
    return face_location


if __name__ == '__main__':
    imgsDir = '/Users/ptrivedi/git-repos/ck_data/cohn-kanade-images'
    labelsDir = '/Users/ptrivedi/git-repos/ck_data/Emotion'
    final_dict = {}

    # Get labels for some images
    for dirPath, subdirList, fileList in os.walk(labelsDir):
        for file in fileList:
            if file[-3:] != 'txt':
                continue
            label_path = os.path.join(dirPath, file)
            print("Reading TEXT file:", file)
            f = open(label_path, 'r')
            contents = f.read()
            f.close()
            final_dict[file[:-12]] = { 'label': int(contents[3])}

    #Get bounding box for some images
    for dirPath, subdirList, fileList in os.walk(imgsDir):
        for file in fileList:
            if file[-3:] != 'png':
                continue
            img_path = os.path.join(dirPath,file)
            print("Reading IMAGE file:", file)
            if file[:-4] in final_dict.keys():
                #print("ENTERED LOGIC")
                final_dict[file[:-4]]['bbox'] = getBoundingBox(img_path)
            else:
                os.remove(img_path)


    #print(final_dict)
    f = open('ck_data.json', 'w')
    json = json.dumps(final_dict)
    f.write(json)
    f.close()






