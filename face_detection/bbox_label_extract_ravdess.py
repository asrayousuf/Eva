import os
from PIL import Image
import face_recognition
import json

def getBoundingBox(img_path):
    image = face_recognition.load_image_file(img_path)
    face_location = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
    return face_location


if __name__ == '__main__':
    imgsDir = '/Users/ptrivedi/git-repos/ravdess-images/ravdess-data'
    final_dict = {}


    #Get bounding box and labels for some images
    for dirPath, subdirList, fileList in os.walk(imgsDir):
        for file in fileList:
            if file[-3:] != 'jpg':
                continue
            img_path = os.path.join(dirPath,file)
            print("Reading IMAGE file:", file)

            #print("ENTERED LOGIC")
            final_dict[file[:-4]] = {'bbox': getBoundingBox(img_path)}


    #print(final_dict)
    f = open('ravdess_data.json', 'w')
    json = json.dumps(final_dict)
    f.write(json)
    f.close()






