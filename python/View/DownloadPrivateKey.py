from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QFileDialog, QMessageBox, QApplication
from PyQt6.QtCore import pyqtSignal
import os

import Encrypt as Prog_Encrypt


class Ui_Form(QWidget):

    privateKey_downloaded = pyqtSignal()

    def __init__(self, private_key, user):
        super(Ui_Form, self).__init__()
        self.private_key = private_key
        self.user = user
        self.selected_folder = None
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
        self.label.setMaximumSize(QtCore.QSize(60, 60))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./picture/key_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setStyleSheet("font-size: 16px;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
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
        self.pushButton.clicked.connect(self.select_folder)

        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.confirm_Btn = QtWidgets.QPushButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.confirm_Btn.setFont(font)
        self.confirm_Btn.setObjectName("confirm_Btn")

        # signal
        self.confirm_Btn.clicked.connect(self.confirm)
        self.confirm_Btn.clicked.connect(Form.close)

        self.verticalLayout.addWidget(self.confirm_Btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
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
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt;\">Download Private Key</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "Your private key is generated. \n"
"Please download the private key file."))
        self.pushButton.setText(_translate("Form", "Choose a folder"))
        self.confirm_Btn.setText(_translate("Form", "Confirm"))

    def download_completed(self):
        self.privateKey_downloaded.emit()

    def select_folder(self):
        self.selected_folder = QFileDialog().getExistingDirectory(self, "Select Directory", "C:\\")
        self.path_input.setText(self.selected_folder)

    def confirm(self):
        if self.selected_folder != None:
            private_key_filename = 'private_key.pem'

            # check if have duplicated file in the destination path
            isDuplicate = True
            base_name, ext = os.path.splitext(private_key_filename)
            count = 0
            while isDuplicate:
                isDuplicate = False
                for filename in os.listdir(self.selected_folder):
                    if filename == private_key_filename:
                        isDuplicate = True
                        count += 1
                        private_key_filename = f"{base_name} ({count}){ext}"
                        break
            privateKey_file = os.path.join(self.selected_folder, private_key_filename)

            # Save the private key file in the selected folder
            Prog_Encrypt.save_private_key(self.private_key, self.user.pwd, privateKey_file)
            while not os.path.isfile(privateKey_file):  # wait until the file finished download
                continue
            QMessageBox.information(None, 
                                    'Successful Download', 
                                    '<html><head/><body><p><span style=\" font-size:15pt;\">Private Key downloaded successfully</span></p></body></html>'
                                    f'<html><head/><body><p><span style=\" font-size:11pt; font-weight:bold;\">{private_key_filename}</span></p></body></html>', 
                                    QMessageBox.StandardButton.Ok, 
                                    QMessageBox.StandardButton.Ok)
            self.download_completed()   # send the download complete signal

