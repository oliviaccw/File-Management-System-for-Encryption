from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox
from PyQt6.QtCore import pyqtSignal
import sys, os

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

from Login import User


class Ui_Form(QWidget):

    privateKey_uploaded = pyqtSignal()

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.file_path = None   # path of upload file
        self.user: User = None
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 399)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(50, 70, 50, 50)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(50, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./picture/oneKey_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 3)
        self.horizontalLayout_2.setStretch(3, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setStyleSheet("font-size: 18px;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path_input = QtWidgets.QLineEdit(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_input.sizePolicy().hasHeightForWidth())
        self.path_input.setSizePolicy(sizePolicy)

        self.path_input.setReadOnly(True)

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.path_input.setFont(font)
        self.path_input.setObjectName("path_input")
        self.horizontalLayout.addWidget(self.path_input)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        # signal
        self.pushButton.clicked.connect(self.select_file)

        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.confirm_Btn = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.confirm_Btn.setFont(font)
        self.confirm_Btn.setObjectName("confirm_Btn")

        # signal
        self.confirm_Btn.clicked.connect(self.confirm)

        self.verticalLayout.addWidget(self.confirm_Btn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(7, 6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt;\">   Upload Private Key</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "\n"
"Please upload your private key file for decryption."))
        self.pushButton.setText(_translate("Form", "Choose a file"))
        self.confirm_Btn.setText(_translate("Form", "Confirm"))

    def select_file(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFile)
        fd.setDirectory('C:\\')
        if fd.exec():
            self.file_path = fd.selectedFiles()[0]
            self.path_input.setText(self.file_path)

    def showCritical(self):
        QMessageBox.critical(None, 
                             'Wrong File', 
                             '<html><head/><body><p><span style=\" font-size:15pt;\">Wrong Private Key File</span></p></body></html>'
                             '<html><head/><body><p><span style=\" font-size:11pt;\">Please upload the correct private key file</span></p></body></html>',
                             QMessageBox.StandardButton.Ok, 
                             QMessageBox.StandardButton.Ok)
        
    def upload_completed(self):
        self.privateKey_uploaded.emit()
        
    def confirm(self):
        if self.file_path != None:
            # Check if the private key is valid
            if os.path.splitext(os.path.basename(self.file_path))[1] == '.pem':
                try:
                    with open(self.file_path, 'rb') as file:
                        private_key = serialization.load_pem_private_key(
                            file.read(),
                            password=self.user.pwd.encode(),
                            backend=default_backend()
                        )
                except: # Given private key file not valid
                    self.showCritical()
                else:   # Given private key file valid
                    self.upload_completed()
            else:   # Not pem file
                self.showCritical()

