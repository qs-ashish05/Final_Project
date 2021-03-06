# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import AddPerson
from main import main
from ANP import Ui_On_click_ANP

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(847, 766)
        self.Add_New_Person = QtWidgets.QPushButton(Dialog)
        self.Add_New_Person.setGeometry(QtCore.QRect(350, 240, 131, 28))
        self.Add_New_Person.setObjectName("Add_New_Person")
        # a = Ui_On_click_ANP()
        # On_click_ANP = QtWidgets.QDialog()
        
        self.Add_New_Person.clicked.connect(lambda : self.Anp())
        #self.Add_New_Person.clicked.connect(lambda : a.setupUi(On_click_ANP))
    

        self.Take_Attendance = QtWidgets.QPushButton(Dialog)
        self.Take_Attendance.setGeometry(QtCore.QRect(350, 290, 131, 28))
        self.Take_Attendance.setObjectName("Take_Attendance")
        m = main()
        self.Take_Attendance.clicked.connect(lambda : m.runCamera())

        self.Exit = QtWidgets.QPushButton(Dialog)
        self.Exit.setGeometry(QtCore.QRect(350, 350, 131, 28))
        self.Exit.setObjectName("Exit")
        self.Exit.clicked.connect(lambda : exit())
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Face Recoginition"))
        self.Add_New_Person.setText(_translate("Dialog", "Add New Person"))
        self.Take_Attendance.setText(_translate("Dialog", "Take Attendance"))
        self.Exit.setText(_translate("Dialog", "Exit"))

    def Anp(self):
        On_click_ANP = QtWidgets.QDialog()
        o = Ui_On_click_ANP()
        o.setupUi(On_click_ANP)
        On_click_ANP.show()
        On_click_ANP.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
