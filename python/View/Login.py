from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication
import sys
import re

from Login import User
import Login as Prog_login

class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.user: User = None    # save the User obj if successful login
        self.config_path = None
        self.folder_path = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(511, 403)
        Form.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.outer_vert = QtWidgets.QVBoxLayout()
        self.outer_vert.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.outer_vert.setContentsMargins(50, 50, 50, 50)
        self.outer_vert.setSpacing(5)
        self.outer_vert.setObjectName("outer_vert")
        self.title_vert = QtWidgets.QVBoxLayout()
        self.title_vert.setObjectName("title_vert")
        self.label = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.title_vert.addWidget(self.label)
        self.outer_vert.addLayout(self.title_vert)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.outer_vert.addItem(spacerItem)
        self.usr_pwd_vert = QtWidgets.QVBoxLayout()
        self.usr_pwd_vert.setSpacing(20)
        self.usr_pwd_vert.setObjectName("usr_pwd_vert")
        self.usrname_hori = QtWidgets.QHBoxLayout()
        self.usrname_hori.setContentsMargins(0, -1, -1, -1)
        self.usrname_hori.setObjectName("usrname_hori")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.usrname_hori.addWidget(self.label_2)
        self.input_username = QtWidgets.QLineEdit(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_username.sizePolicy().hasHeightForWidth())
        self.input_username.setSizePolicy(sizePolicy)
        self.input_username.setMaximumSize(QtCore.QSize(16777215, 50))
        self.input_username.setObjectName("input_username")
        self.usrname_hori.addWidget(self.input_username)
        self.usrname_hori.setStretch(0, 1)
        self.usrname_hori.setStretch(1, 9)
        self.usr_pwd_vert.addLayout(self.usrname_hori)
        self.pwd_hori = QtWidgets.QHBoxLayout()
        self.pwd_hori.setObjectName("pwd_hori")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.pwd_hori.addWidget(self.label_3)
        self.input_pwd = QtWidgets.QLineEdit(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_pwd.sizePolicy().hasHeightForWidth())
        self.input_pwd.setSizePolicy(sizePolicy)
        self.input_pwd.setMaximumSize(QtCore.QSize(16777215, 50))
        self.input_pwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.input_pwd.setObjectName("input_pwd")
        self.pwd_hori.addWidget(self.input_pwd)
        self.pwd_hori.setStretch(0, 1)
        self.pwd_hori.setStretch(1, 9)
        self.usr_pwd_vert.addLayout(self.pwd_hori)
        self.outer_vert.addLayout(self.usr_pwd_vert)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.outer_vert.addItem(spacerItem1)
        self.button_signal_vert = QtWidgets.QVBoxLayout()
        self.button_signal_vert.setSpacing(5)
        self.button_signal_vert.setObjectName("button_signal_vert")
        self.button_hori = QtWidgets.QHBoxLayout()
        self.button_hori.setContentsMargins(-1, 0, -1, -1)
        self.button_hori.setSpacing(16)
        self.button_hori.setObjectName("button_hori")
        self.sigin_Btn = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sigin_Btn.sizePolicy().hasHeightForWidth())
        self.sigin_Btn.setSizePolicy(sizePolicy)
        self.sigin_Btn.setStyleSheet("font-size: 14px;")
        self.sigin_Btn.setObjectName("sigin_Btn")

        # signal for sign in 
        self.sigin_Btn.clicked.connect(self.signIn)

        self.button_hori.addWidget(self.sigin_Btn)
        self.signup_Btn = QtWidgets.QPushButton(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signup_Btn.sizePolicy().hasHeightForWidth())
        self.signup_Btn.setSizePolicy(sizePolicy)
        self.signup_Btn.setStyleSheet("font-size: 14px;")
        self.signup_Btn.setObjectName("signup_Btn")

        # signal for sign up 
        self.signup_Btn.clicked.connect(self.signUp)

        self.button_hori.addWidget(self.signup_Btn)
        self.button_signal_vert.addLayout(self.button_hori)
        self.signal_label = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signal_label.sizePolicy().hasHeightForWidth())
        self.signal_label.setSizePolicy(sizePolicy)
        self.signal_label.setStyleSheet("font-weight: bold; color:Tomato; font-size: 16px;")
        self.signal_label.setText("")
        self.signal_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.signal_label.setWordWrap(True)
        self.signal_label.setObjectName("signal_label")
        self.button_signal_vert.addWidget(self.signal_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.button_signal_vert.addItem(spacerItem2)
        self.button_signal_vert.setStretch(0, 2)
        self.button_signal_vert.setStretch(1, 4)
        self.button_signal_vert.setStretch(2, 3)
        self.outer_vert.addLayout(self.button_signal_vert)
        self.outer_vert.setStretch(0, 2)
        self.outer_vert.setStretch(2, 2)
        self.outer_vert.setStretch(4, 3)
        self.verticalLayout_2.addLayout(self.outer_vert)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "File Management System"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">File Management System</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">Username:</span></p></body></html>"))
        self.input_username.setPlaceholderText(_translate("Form", "Enter your username"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">Password: </span></p></body></html>"))
        self.input_pwd.setPlaceholderText(_translate("Form", "Enter your password"))
        self.sigin_Btn.setText(_translate("Form", "Sign in"))
        self.signup_Btn.setText(_translate("Form", "Sign up"))

    def signIn(self):
        username = self.input_username.text().strip()
        pwd = self.input_pwd.text().strip()
        
        if username == '' or pwd == '':
            self.signal_label.setStyleSheet("font-weight: bold; color:Tomato; font-size: 16px;")
            self.signal_label.setText('Username or password cannot be empty.')
        else:
            user = User(username, pwd) 
            result = Prog_login.signIn(self.config_path, user)
            if result[0] == False:
                self.signal_label.setStyleSheet("font-weight: bold; color:Tomato; font-size: 16px;")
                self.signal_label.setText(result[1])
            else:   # successful login
                self.signal_label.setStyleSheet("font-weight: bold; color:green; font-size: 16px;")
                self.signal_label.setText("Successful login!")
                self.user = user
                username = None
                pwd = None
                self.close()
                

    def signUp(self):
        username = self.input_username.text().strip()
        pwd = self.input_pwd.text().strip()
        special_char = r'[!@#$%^&*(),.?":{}|<>[\]]'

        if username == '' or pwd == '':
            self.signal_label.setStyleSheet("font-weight: bold; color:Tomato; font-size: 16px;")
            self.signal_label.setText('Username or password cannot be empty.')
        elif re.search(special_char, username):
            self.signal_label.setStyleSheet("font-weight: bold; color:Tomato; font-size: 16px;")
            self.signal_label.setText('Username cannot contain any special character: \n[]!@#$%^&*(),.?":{}|<>')
        else:
            user = User(username, pwd)
            result = Prog_login.signUp(self.config_path, user)
            if result[0] == False:
                self.signal_label.setStyleSheet("font-weight: bold; color:Tomato; font-size: 16px;")
                self.signal_label.setText(result[1])
            else:
                self.signal_label.setStyleSheet("font-weight: bold; color:green; font-size: 16px;")
                self.signal_label.setText('Registration successful!')
                self.input_username.setText('')
                self.input_pwd.setText('')
                Prog_login.build_user_folder(self.folder_path, username)
        username = None
        pwd = None

