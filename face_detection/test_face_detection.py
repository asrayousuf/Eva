from PIL import Image
from detector import detect_faces
import os, glob

path = "./data/AgeDB/*.jpg"

for img_file in glob.glob(path):
    im = Image.open(img_file)
    bounding_boxes, landmarks = detect_faces(im)
    print("For file", img_file, "the bounding boxes are:", str(bounding_boxes))
