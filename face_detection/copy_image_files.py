import os
from shutil import copyfile

if __name__ == '__main__':
    imgsDir = '/Users/ptrivedi/git-repos/ck_data/emotion_images'
    newDirPath = '/Users/ptrivedi/git-repos/ck_data/final_emotion_images'

    #os.mkdir(newDirPath)
    for dirPath, subdirList, fileList in os.walk(imgsDir):
        for file in fileList:
            if file[-3:] != 'png':
                continue
            img_path = os.path.join(dirPath, file)
            new_img_path = os.path.join(newDirPath, file)
            print("Copying file:", file)
            copyfile(img_path, new_img_path)

    print("DONE")
