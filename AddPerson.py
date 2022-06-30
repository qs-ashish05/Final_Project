import cv2
import os
import numpy as np
from Gui import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets


def AddPerson(name,roll):
    # name = input("Enter name of person : ")
    # roll = input("Enter Roll_no. of the person : ")
    
    name = name
    roll = roll
    #cwd = os.getcwd()
    #train.var = cwd
    img = str(roll)+"_"+name

    
    #os.mkdir("Store_images")
    os.chdir("Training_images")

    #var = os.getcwd()

    #os.mkdir(dir)
    #os.chdir(dir)
    #cwd1 = os.getcwd()

    # print("here images are stored")
    # print(cwd1)

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Python webcamp screenshot app")

    img_counter = 0

    while img_counter < 10:
        ret,frame = cam.read()

        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow("test",frame)

        k = cv2.waitKey(1)

        for i in range(10):
            if k%256 == 27:
                print("Escape hit, closing the app")
                break

            elif k%256 == 32:
                
                img_name = img+".png"
                cv2.imwrite(img_name,frame)
                print("screen shot taken")
                img_counter = img_counter + 1

    cam.release()
    os.chdir("../")
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()
    #exit(0)
    #cam.destroyAllWindows()

