from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox
import os

from Login import User
import Encrypt as Prog_Encrypt
import View.UploadPrivateKey as UploadPrivateKey


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.filename = None       # path of file that need to be decripted
        self.encrypt_type = None
        self.users_path = None
        self.user: User = None
        self.private_key_file = None
        self.mainWindow_self = None
        self.selected_folder = None
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 413)
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
        self.label.setPixmap(QtGui.QPixmap("./picture/download_file_icon.png"))
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

        self.verticalLayout.addWidget(self.confirm_Btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(6, 6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt;\">Download Decrypted File</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Choose a folder"))
        self.confirm_Btn.setText(_translate("Form", "Confirm"))

    def select_folder(self):
        self.selected_folder = QFileDialog().getExistingDirectory(self, "Select Directory", "C:\\")
        self.path_input.setText(self.selected_folder)

    def confirm(self):
        if self.selected_folder != None:
            download_file_name = self.filename.rsplit(".bin", 1)[0]
            # check if have duplicated file in the destination path
            isDuplicate = True
            base_name, ext = os.path.splitext(download_file_name)
            count = 0
            while isDuplicate:
                isDuplicate = False
                for filename in os.listdir(self.selected_folder):
                    if filename == download_file_name:
                        isDuplicate = True
                        count += 1
                        download_file_name = f"{base_name} ({count}){ext}"
                        break
            output_file = os.path.join(self.selected_folder, download_file_name)
            
            if self.encrypt_type == 'Passphrase Encrypted':
                file_path = os.path.join(self.users_path, self.user.username, 'passEncrypt', f"{self.filename}.bin")
                Prog_Encrypt.decrypt_file_with_pwd(file_path, output_file, self.user.pwd)
                while not os.path.isfile(output_file):
                    continue
                self.showSuccess(download_file_name)
            elif self.encrypt_type == 'Public Key Encrypted':
                file_path = os.path.join(self.users_path, self.user.username, 'keyEncrypt', 'files', f"{self.filename}.bin")
                fileKey_path = os.path.join(self.users_path, self.user.username, 'keyEncrypt', 'keys', f"{self.filename}.bin")
                try:
                    Prog_Encrypt.decrypt_file_with_RSA_AES(file_path, output_file, self.private_key_file, fileKey_path, self.user.pwd)
                except:     # the private key is wrong
                    QMessageBox.critical(None, 
                             'Wrong File', 
                             '<html><head/><body><p><span style=\" font-size:15pt;\">Wrong Private Key File</span></p></body></html>'
                             '<html><head/><body><p><span style=\" font-size:11pt;\">File cannot be decrypted by the given private key file.\nPlease upload the correct private key file.</span></p></body></html>',
                             QMessageBox.StandardButton.Ok, 
                             QMessageBox.StandardButton.Ok)
                    self.upload_privateKey_window = UploadPrivateKey.Ui_Form()
                    self.upload_privateKey_window.user = self.user
                    self.upload_privateKey_window.show()
                    self.upload_privateKey_window.privateKey_uploaded.connect(self.get_privateKey_file)
                    self.upload_privateKey_window.privateKey_uploaded.connect(self.upload_privateKey_window.hide)
                else:
                    while not os.path.isfile(output_file):
                        continue
                    self.showSuccess(download_file_name)
            else:
                QMessageBox.information(None, 
                                '<html><head/><body><p><span style=\" font-size:15pt;\">Error</span></p></body></html>', 
                                '<html><head/><body><p><span style=\" font-size:11pt;\">Error of pending the file encryption type</span></p></body></html>', 
                                QMessageBox.StandardButton.Ok, 
                                QMessageBox.StandardButton.Ok)
                
                
    def get_privateKey_file(self):
        self.private_key_file = self.upload_privateKey_window.file_path
        self.mainWindow_self.private_key_file = self.upload_privateKey_window.file_path


    def showSuccess(self, download_file_name):
        QMessageBox.information(None, 
                                'Successful Download', 
                                '<html><head/><body><p><span style=\" font-size:15pt;\">File downloaded successfully</span></p></body></html>' 
                                f'<html><head/><body><p><span style=\" font-size:11pt; font-weight:bold;\">{download_file_name}</span></p></body></html>', 
                                QMessageBox.StandardButton.Ok, 
                                QMessageBox.StandardButton.Ok)
