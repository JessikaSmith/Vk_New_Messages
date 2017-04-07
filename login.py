# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.6

from vk_app import vkontakte

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def loginCheck(self):
        id = self.idEdit.text()
        userlogin = self.loginEdit_3.text()
        userpassword = self.passEdit_2.text()
        self.vk_conn = vkontakte(id, userlogin,userpassword)
        text = self.vk_conn.get_last_messages()
		
        for i in range(1,10):
            if text[i]['read_state'] == 1:
                if i == 1:
                    print('Нет непрочитанных сообщений')
                break
            user_info = api.users.get(user_ids = text[i]['uid'])
            print(user_info[0]['last_name'] + ' ' + user_info[0]['first_name']+': '+text[i]['body'] )
            # print(text[i])
            try:
                attachment = text[i]['attachment']
                print(attachment['type'])
            except KeyError:
                pass
		
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 247)
        Dialog.setStyleSheet("QDialog{\n"
"background-color:rgb(229, 221, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:rgb(125, 60, 255);\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.id_app = QtWidgets.QLabel(Dialog)
        self.id_app.setGeometry(QtCore.QRect(10, 60, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.id_app.setFont(font)
        self.id_app.setTextFormat(QtCore.Qt.AutoText)
        self.id_app.setScaledContents(False)
        self.id_app.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.id_app.setObjectName("id_app")
        self.idEdit = QtWidgets.QLineEdit(Dialog)
        self.idEdit.setGeometry(QtCore.QRect(160, 60, 113, 20))
        self.idEdit.setObjectName("idEdit")
        self.login = QtWidgets.QLabel(Dialog)
        self.login.setGeometry(QtCore.QRect(60, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setTextFormat(QtCore.Qt.AutoText)
        self.login.setScaledContents(False)
        self.login.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login.setObjectName("login")
        self.passw = QtWidgets.QLabel(Dialog)
        self.passw.setGeometry(QtCore.QRect(60, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.passw.setFont(font)
        self.passw.setTextFormat(QtCore.Qt.AutoText)
        self.passw.setScaledContents(False)
        self.passw.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passw.setObjectName("passw")
        self.passEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.passEdit_2.setGeometry(QtCore.QRect(160, 140, 113, 20))
        self.passEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passEdit_2.setObjectName("passEdit_2")
        self.loginEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.loginEdit_3.setGeometry(QtCore.QRect(160, 100, 113, 20))
        self.loginEdit_3.setObjectName("loginEdit_3")
        self.OKButton = QtWidgets.QPushButton(Dialog)
        self.OKButton.setGeometry(QtCore.QRect(200, 200, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setBold(True)
        font.setWeight(75)
        self.OKButton.setFont(font)
        self.OKButton.setObjectName("OKButton")
		#### событие для кнопки ОК ####
        self.OKButton.clicked.connect(self.loginCheck)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.id_app.setText(_translate("Dialog", "id приложения"))
        self.login.setText(_translate("Dialog", "логин"))
        self.passw.setText(_translate("Dialog", "пароль"))
        self.OKButton.setText(_translate("Dialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

