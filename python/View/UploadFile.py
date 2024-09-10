from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox
import sys, os

import FileManage as Prog_FileManage
import Encrypt as Prog_Encrypt
from Login import User
import View.DownloadPrivateKey


class Ui_Form(QWidget):

    def __init__(self, mainWindow_self):
        super(Ui_Form, self).__init__()
        self.file_path = None   # path of upload file
        self.users_path = None
        self.user: User = None
        self.mainWindow_self = mainWindow_self
        self.pubKey = None
        self.pubKey_file = None     # file path for save the public key
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
        self.label.setPixmap(QtGui.QPixmap("./picture/upload_file_icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(1, 5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.passEncrypt_Btn = QtWidgets.QRadioButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.passEncrypt_Btn.setFont(font)
        self.passEncrypt_Btn.setObjectName("passEncrypt_Btn")
        self.horizontalLayout_3.addWidget(self.passEncrypt_Btn)
        self.pubKeyEncrypt_Btn = QtWidgets.QRadioButton(parent=Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pubKeyEncrypt_Btn.setFont(font)
        self.pubKeyEncrypt_Btn.setObjectName("pubKeyEncrypt_Btn")
        self.horizontalLayout_3.addWidget(self.pubKeyEncrypt_Btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
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
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(7, 6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "File Management System"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt;\">Upload File</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Choose a file"))
        self.passEncrypt_Btn.setText(_translate("Form", "Password Encryption"))
        self.pubKeyEncrypt_Btn.setText(_translate("Form", "Public Key Encryption"))
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
                             'Duplicate File', 
                             "<html><head/><body><p><span style=\" font-size:15pt;\">Duplicate File</span></p></body></html>"
                             "<html><head/><body><p><span style=\" font-size:11pt;\">A file with the same name already exists in the File Management System, so it cannot be uploaded.</span></p></body></html>",
                             QMessageBox.StandardButton.Ok, 
                             QMessageBox.StandardButton.Ok)

    def confirm(self):
        # get the encrypt choice
        if self.passEncrypt_Btn.isChecked():
            encrypt_choice = 'pass'
        elif self.pubKeyEncrypt_Btn.isChecked():
            encrypt_choice = 'pubKey'
        else:
            encrypt_choice = None

        # user chose the file and encrypt way
        if self.file_path != None and encrypt_choice != None:
            if encrypt_choice == 'pass':
                ouput_folder_path = os.path.join(self.users_path, self.user.username, 'passEncrypt')
                filename = Prog_FileManage.check_duplicate(self.file_path, ouput_folder_path)
                if filename == None:    # have duplicate file
                    self.showCritical()
                else:
                    # set the output file directory and name
                    output_file = os.path.join(ouput_folder_path, filename + '.bin')
                    Prog_Encrypt.encrypt_file_with_pwd(self.file_path, output_file, self.user.pwd)
                    self.mainWindow_self.initialFileList()  # Reflesh the file list
                    self.messageBox = QMessageBox.information(None, 
                                                              'Successful Upload', 
                                                              '<html><head/><body><p><span style=\" font-size:15pt;\">Successful Upload</span></p></body></html>'
                                                              '<html><head/><body><p><span style=\" font-size:11pt;\">File uploaded successfully</span></p></body></html>', 
                                                              QMessageBox.StandardButton.Ok, 
                                                              QMessageBox.StandardButton.Ok)
                    
            else:   # encrypt_choice = 'pubKey'
                # check whether the user has generate public key before
                user_config_path = os.path.join(self.users_path, self.user.username, 'config')
                self.pubKey_file = os.path.join(user_config_path, 'pubKey.pem')
                if not os.path.isfile(self.pubKey_file):     # If the user didn't generate pubKey before
                    # Generate the private key & public key
                    privateKey, self.pubKey = Prog_Encrypt.generate_key_pair()
                    # Open the DownloadPrivateKey window for user to download the private key
                    self.privateKey_window = View.DownloadPrivateKey.Ui_Form(privateKey, self.user)
                    self.privateKey_window.show()
                    self.privateKey_window.privateKey_downloaded.connect(self.save_pubKey)
                    self.privateKey_window.privateKey_downloaded.connect(self.pubKey_encryption)
                else:
                    self.pubKey_encryption()
                        
                        
    def save_pubKey(self):
        # save the public key in user's config folder
        Prog_Encrypt.save_public_key(self.pubKey, self.pubKey_file)
     
    def pubKey_encryption(self):
        # public key encryption part
        output_file_folder_path = os.path.join(self.users_path, self.user.username, 'keyEncrypt', 'files')
        output_fileKey_folder_path = os.path.join(self.users_path, self.user.username, 'keyEncrypt', 'keys')
        filename = Prog_FileManage.check_duplicate(self.file_path, output_file_folder_path)
        if filename == None:    # have duplicate file
            self.showCritical()
        else:   # Encrypt and save the file
            self.pubKey_file = os.path.join(self.users_path, self.user.username, 'config', 'pubKey.pem')
            Prog_Encrypt.encrypt_file_with_RSA_AES(self.file_path, output_file_folder_path, self.pubKey_file, output_fileKey_folder_path)

            self.mainWindow_self.initialFileList()  # Reflesh the file list
            self.messageBox = QMessageBox.information(None, 
                                                      'Successful Upload', 
                                                      '<html><head/><body><p><span style=\" font-size:15pt;\">Successful Upload</span></p></body></html>'
                                                      '<html><head/><body><p><span style=\" font-size:11pt;\">File uploaded successfully</span></p></body></html>', 
                                                      QMessageBox.StandardButton.Ok, 
                                                      QMessageBox.StandardButton.Ok)


