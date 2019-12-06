import os
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

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

def extractImagesWithoutBlink(path, filename):
    full_path = 'videos/' + path + '/'
    cap = cv2.VideoCapture(full_path + filename)
    count = 0
    while True:
        cap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
        ret, image = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        if len(faces) > 0:
            frame_tmp = image[faces[0][1]:faces[0][1] + faces[0][3], faces[0][0]:faces[0][0] + faces[0][2]:1, :]
            frame = frame[faces[0][1]:faces[0][1] + faces[0][3], faces[0][0]:faces[0][0] + faces[0][2]:1]
            eyes = eyeCascade.detectMultiScale(
                frame,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(100, 100)
            )
            if len(eyes) > 0:
                cv2.imwrite('videos/' + path + '/' + "{}-{}.jpg".format(filename[:-4], count), image)
        count = count + 1

if __name__=="__main__":
    for folder in mapping.values():
        for filename in os.listdir('videos/' + folder):
            if filename.endswith('.mp4'):
                extractImagesWithoutBlink(folder, filename)
                print('done extracting images for {}'.format(filename))
                os.remove('videos/' + folder + '/' + filename)
