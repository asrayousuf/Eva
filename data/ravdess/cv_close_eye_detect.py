import os
import cv2

eye_cascPath = 'haarcascade_eye_tree_eyeglasses.xml'
face_cascPath = 'haarcascade_frontalface_alt.xml'
faceCascade = cv2.CascadeClassifier(face_cascPath)
eyeCascade = cv2.CascadeClassifier(eye_cascPath)

def extractImagesWithoutBlink(pathIn):
    cap = cv2.VideoCapture(pathIn)
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
                cv2.imwrite("{}-{}.jpg".format(pathIn[:-4], count), image)
        count = count + 1

if __name__=="__main__":
    for filename in os.listdir('.'):
        if filename.endswith('.mp4'):
            extractImagesWithoutBlink(filename)
            print('done extracting images for {}'.format(filename))
