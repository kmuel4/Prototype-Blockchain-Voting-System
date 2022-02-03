#This program requires a database of images to run, all file locations are placeholders, and serves as an example 
#of how the code would look and run

import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

#Loop for all possible voters
for i in os.listdir(path):
    voters.append(i)
    
features = np.load('features.npy')
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('C:\Users\Default\Faces\currentvoter.jpg)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Voter', gray)

#Find face in image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    
    label, confidence = face_recognizer.predict(faces_roi)
 
#Return true fals based on id match and confidence level

if label == voter and confidence > "50";
    return true
else
    return false
   