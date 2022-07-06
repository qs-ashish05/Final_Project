import cv2
import numpy as np
import pandas as pd
import face_recognition
import os
from datetime import date
import write_csv


# from PIL import ImageGrab


class main(object):
    def __init__(self):
        self.path = 'Training_images'
        self.images = []
        self.classNames = []
        self.myList = os.listdir(self.path)
        # print(myList)
        for cl in self.myList:
            curImg = cv2.imread(f'{self.path}/{cl}')
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])
        # print(classNames)
        self.encodeListKnown = self.findEncodings(self.images)
        print('Encoding Complete')


    def findEncodings(self, images):
        encodeList = []

        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img) #[0]
            encodeList.append(encode)
        return encodeList


    def markAttendance(self, name):

        #print("Hi")
        nameList = []

        nameList.append(name)

        today = date.today()
        DATE = today.strftime("%m/%d/%y")

        column = {DATE : nameList}

        df = pd.DataFrame(column,columns=[DATE])

        df.to_csv(f"Attendane_of_Today.csv")
        #print('File is generated')
           # print(name)
            #write_csv.Write_in_csv(nameList)

            ###if name not in nameList:
                #now = datetime.now()
                #dtString = now.strftime('%H:%M:%S')
                #f.writelines(f'\n{name},')
                ###write_csv.Write_in_csv(nameList)

           

    #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
    # def captureScreen(bbox=(300,300,690+300,530+300)):
    #     capScr = np.array(ImageGrab.grab(bbox))
    #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    #     return capScr



    def runCamera(self):
        cap = cv2.VideoCapture(0)
        while True:
            success, img = cap.read()
        # img = captureScreen()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
        # print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = self.classNames[matchIndex].upper()
        # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    self.markAttendance(name)

            cv2.imshow('Webcam', img)
            cv2.waitKey(1)