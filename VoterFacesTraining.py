#The following program does not run, as we would have to create a matching dataset for all 1000 voters, each with indiviidual 
#faces to match the names. All directories are just placeholders.

import os
import cv2 as cv
import numpy as np 

#Set path variable for ease of use later

path = "/Users/Default/Documents/Voters/Faces/Train"
haar_cascasde = cv.CascadeClassifier('haar_face.xml')

#Create Empty List
voters = []


#Fill List with all registered voter numbers
for i in os.listdir(path):
    voters.append(i)
    
  DIR = path

  features = []
  labels = []
  
  def create_train():
    for voter in voters:
        voterpath = os.voterpath.join(DIR, voter)
        label = voters.index(voter)
        
        for img in os.listdir(voterpath):
            img_path = os.path.join(voterpath, img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascasde.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
                
  create_train()
  
  face_recognizer.save('face_trained.yml')
  features = np.array(features, dtype='object')
  labels = np.array(labes)
  face_recognizer = cv.face.LBPHFaceRecognizer_create()
  
  #Train Recognizer on features list and lebel list
  face_recognizer.train(features.labels)
  
  np.save('features.npy', features)
  np.save('labels.npy', labels)
  