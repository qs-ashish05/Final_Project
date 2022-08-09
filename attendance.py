import os
import cv2
import time
import numpy as np
import pandas as pd
import face_recognition
from datetime import date, datetime
from PIL import Image as im
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_On_click_Take_Attendance(object):
    def setupUi(self, On_click_Take_Attendance):
        self.On_click_Take_Attendance = On_click_Take_Attendance
        self.On_click_Take_Attendance.setObjectName("On_click_Take_Attendance")
        self.On_click_Take_Attendance.setFixedSize(700, 500)
        self.img_label = QtWidgets.QLabel(On_click_Take_Attendance)
        self.img_label.setGeometry(QtCore.QRect(60, 10, 590, 370))
        self.img_label.setText("")
        self.img_label.setScaledContents(True)
        self.img_label.setObjectName("img_label")
        self.take_attendance_btn = QtWidgets.QPushButton(self.On_click_Take_Attendance)
        self.take_attendance_btn.setGeometry(QtCore.QRect(300, 450, 100, 25))
        self.take_attendance_btn.setObjectName("take_attendance_btn")
        self.take_attendance_btn.clicked.connect(lambda: self.close())
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.On_click_Take_Attendance)

        # create a timer
        self.timer = QtCore.QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.take_attendance_btn.clicked.connect(lambda: self.close())
        os.chdir('..')
        
        self.path = 'Training_images'
        self.images = []
        self.classNames = []
        self.myList = os.listdir(self.path)
        for cl in self.myList:
            curImg = cv2.imread(f'{self.path}/{cl}')
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])
        self.encodeListKnown = self.findEncodings()
        print('Encoding Complete')


    def findEncodings(self):
        encodeList = []
        for img in self.images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList


    def markAttendance(self, name):
        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readlines()

            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    f.writelines(f'\n{name},{dtString}')

#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr




    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.On_click_Take_Attendance.setWindowTitle(_translate("On_click_Take_Attendance", "ANP"))
        self.take_attendance_btn.setText(_translate("On_click_Take_Attendance", "Stop"))
        return


    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        imgS = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        # imgS = cv2.resize(imgS, (0, 0), None, 0.25, 0.25)
        height, width, channel = imgS.shape
        step = channel * width
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
    # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = self.classNames[matchIndex].upper()
    # print(name)
                y1, x2, y2, x1 = faceLoc
                # uncomment this if uncommenting line 96. Makes image blurry but is lighter on system
                # y1, x2, y2, x1 = int(y1 / 4), int(x2 / 4), int(y2 / 4), int(x1 / 4)
                y1, x2, y2, x1 = int(y1), int(x2), int(y2), int(x1)
                imgS = cv2.rectangle(imgS, (x1, y1), (x2, y2), (0, 255, 0), 1)
                imgS = cv2.rectangle(imgS, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                imgS = cv2.putText(imgS, name, (x1 + 6, y2), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 1)
                self.markAttendance(name)

        # create QImage from image
        qImg = QtGui.QImage(imgS, width, height, step, QtGui.QImage.Format_RGB888)
        # show image in img_label
        self.img_label.setPixmap(QtGui.QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()