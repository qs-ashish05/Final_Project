# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ANP.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os
import numpy as np
from PIL import Image as im

class Ui_On_click_ANP(object):
    def setupUi(self, On_click_ANP):
        self.On_click_ANP = On_click_ANP
        self.On_click_ANP.setObjectName("On_click_ANP")
        self.On_click_ANP.setFixedSize(700, 500)
        self.Name = QtWidgets.QTextEdit(self.On_click_ANP)
        self.Name.setGeometry(QtCore.QRect(50, 390, 220, 30))
        self.Name.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.Name.setTabChangesFocus(True)
        self.Name.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.Name.setObjectName("Name")
        self.Roll = QtWidgets.QTextEdit(self.On_click_ANP)
        self.Roll.setGeometry(QtCore.QRect(430, 390, 220, 30))
        self.Roll.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhMultiLine)
        self.Roll.setTabChangesFocus(True)
        self.Roll.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.Roll.setObjectName("Roll")
        self.img_label = QtWidgets.QLabel(On_click_ANP)
        self.img_label.setGeometry(QtCore.QRect(10, 10, 680, 370))
        self.img_label.setText("")
        self.img_label.setScaledContents(True)
        self.img_label.setObjectName("img_label")
        self.Ok_btn = QtWidgets.QPushButton(self.On_click_ANP)
        self.Ok_btn.setGeometry(QtCore.QRect(380, 450, 80, 25))
        self.Ok_btn.setObjectName("Ok_btn")
        self.add_entry_btn = QtWidgets.QPushButton(self.On_click_ANP)
        self.add_entry_btn.setGeometry(QtCore.QRect(200, 450, 80, 25))
        self.add_entry_btn.setObjectName("add_entry_btn")
        self.startCam()

        self.Ok_btn.clicked.connect(lambda: self.close())
        self.add_entry_btn.clicked.connect(lambda: self.AddPerson())
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.On_click_ANP)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.On_click_ANP.setWindowTitle(_translate("On_click_ANP", "ANP"))
        self.Name.setPlaceholderText(_translate("On_click_ANP", "Enter Name : "))
        self.Roll.setPlaceholderText(_translate("On_click_ANP", "Enter Roll No : "))
        self.Ok_btn.setText(_translate("On_click_ANP", "Ok"))
        self.add_entry_btn.setText(_translate("On_click_ANP", "Take Photo"))

    def startCam(self):
        cam = cv2.VideoCapture(0)
        os.chdir("Training_images")
        while True:
            ret,frame = cam.read()
            if ret:
                data = im.fromarray(frame)
                ## save the image file as png
                data.save('image.png')
                ##display saved image in Qpixmap
                self.img_label.setPixmap(QtGui.QPixmap("image.png"))
                if (self.Name.toPlainText() != "") and (self.Roll.toPlainText() != ""):
                    self.add_entry_btn.setEnabled(True)
                    break
                else:
                    self.add_entry_btn.setEnabled(False)
                self.add_entry_btn.clicked.connect(lambda: AddPerson())


    def AddPerson(self):
        # name = input("Enter name of person : ")
        # roll = input("Enter Roll_no. of the person : ")
        
        name = self.Name.toPlainText()
        roll = self.Roll.toPlainText()
        img = str(roll)+"_"+name

        img_name = img+".png"
        cv2.imwrite(img_name,frame)
        print("screen shot taken")
        img_counter = img_counter + 1    