from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem, QColor
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QMainWindow, QHeaderView, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtWidgets import QVBoxLayout, QFrame
from PyQt6.QtCore import Qt

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import sys, os

import View.UploadFile as UploadFile
import View.DownloadDecryptedFile as DownloadDecryptedFile
import View.UploadPrivateKey as UploadPrivateKey
import View.Encryption as Encryption
import View.KeyGeneration as KeyGeneration
from Login import User
import FileManage as Prog_FileManage
import Login as Prog_login


class Ui_MainWindow(QMainWindow):

    def __init__(self, users_path, user):
        super(Ui_MainWindow, self).__init__()
        # not show maximize window option
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.setupUi(self)
        self.users_path = users_path
        self.user: User = user
        self.private_key_file = None
        self.toBeDecryptFile = None
        self.initialFileList()

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 750)
        icon = QtGui.QIcon()
        #*
        icon.addPixmap(QtGui.QPixmap("./picture/folder_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #* Tree View
        self.treeView = QtWidgets.QTreeView(parent=self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 1011, 651))
        self.treeView.setUniformRowHeights(True)
        self.treeView.setAnimated(True)
        self.treeView.setObjectName("treeView")
        
        #? Set model for Tree View
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Size', 'Date Modified'])

        self.fileType1 = QStandardItem('Passphrase Encrypted')
        self.fileType1.setFlags(self.fileType1.flags() & ~Qt.ItemFlag.ItemIsEditable)
        # self.fileType1.appendRow(
        #     [QStandardItem(''), QStandardItem(''), QStandardItem('')]
        # )
        
        self.model.appendRow(self.fileType1)

        self.fileType2 = QStandardItem('Public Key Encrypted')
        self.fileType2.setFlags(self.fileType2.flags() & ~Qt.ItemFlag.ItemIsEditable)
        # self.fileType2.appendRow(
        #     [QStandardItem('test2.txt'), QStandardItem('2Kb'), QStandardItem('6-4-2024')]
        # )
        self.model.appendRow(self.fileType2)

        self.treeView.setModel(self.model)
        # Set column width for column 0 ('Name')
        column0_width = 300
        self.treeView.header().setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)
        self.treeView.header().resizeSection(0, column0_width)
        # column1_width = 300
        # self.treeView.header().setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)
        # self.treeView.header().resizeSection(1, column1_width)
        self.treeView.expandAll()
        #* End of Tree View

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")

        #* Add buttom to the Tool Bar
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(35, 35))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.upload_file_Btn = self.toolBar.addAction(QIcon("./picture/upload_file_icon.png"), "Upload File")
        self.upload_file_Btn.setObjectName("upload_file_Btn")
        #? signal for upload file
        self.upload_file_Btn.triggered.connect(self.upload_file)

        self.toolBar.addSeparator()
        self.download_Btn = self.toolBar.addAction(QIcon("./picture/download_icon.png"), "Download \nDecrypted File")
        self.download_Btn.setObjectName("downlaod_Btn")

        #? signal for upload file
        self.download_Btn.triggered.connect(self.download_decrypt_file)

        self.toolBar.addSeparator()
        self.delete_Btn = self.toolBar.addAction(QIcon("./picture/delete_icon.png"), "Delete")
        self.delete_Btn.setObjectName("delete_Btn")

        #? signal for delete file
        self.delete_Btn.triggered.connect(self.delete_file)

        self.toolBar.addSeparator()


        # Add a separator widget
        separator_widget1 = QFrame()
        separator_widget1.setFrameShape(QFrame.Shape.HLine)
        separator_widget1.setFrameShadow(QFrame.Shadow.Sunken)
        separator_widget1.setFixedHeight(2)  # Adjust the separator height if needed
        separator_widget1.setStyleSheet("background-color: black;")
        self.toolBar.addWidget(separator_widget1)


        self.toolBar.addSeparator()
        self.encryption_Btn = self.toolBar.addAction(QIcon("./picture/lock_icon.png"), "Encryption")
        self.encryption_Btn.setObjectName("encryption_Btn")
        self.toolBar.addSeparator()

        #? signal for encryption btn
        self.encryption_Btn.triggered.connect(self.encryption)

        self.keyGenerate_Btn = self.toolBar.addAction(QIcon("./picture/oneKeyRev_icon.png"), "Generate\nKeys")
        self.keyGenerate_Btn.setObjectName("keyGenerate_Btn")
        self.toolBar.addSeparator()

        #? signal for key generation btn
        self.keyGenerate_Btn.triggered.connect(self.keyGeneration)

        # Add a separator widget
        separator_widget2 = QFrame()
        separator_widget2.setFrameShape(QFrame.Shape.HLine)
        separator_widget2.setFrameShadow(QFrame.Shadow.Sunken)
        separator_widget2.setFixedHeight(2)  # Adjust the separator height if needed
        separator_widget2.setStyleSheet("background-color: black;")
        self.toolBar.addWidget(separator_widget2)
        
        self.toolBar.addSeparator()
        self.logout_Btn = self.toolBar.addAction(QIcon("./picture/logout_icon.png"), "Log out")
        self.logout_Btn.setObjectName("logout_Btn")

        #? signal for logout
        self.logout_Btn.triggered.connect(self.logout)
        #*

        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Management System"))
        

    def upload_file(self):
        # app = QApplication(sys.argv)
        # open upload file window
        self.upload_file_window = UploadFile.Ui_Form(self)
        # pass data to upload file ui
        self.upload_file_window.users_path = self.users_path
        self.upload_file_window.user = self.user
        self.upload_file_window.show()

    def delete_file(self):
        selected_item = self.treeView.selectedIndexes()
        if selected_item and selected_item[0].parent().data(Qt.ItemDataRole.DisplayRole) != None:
            filename = selected_item[0].data(Qt.ItemDataRole.DisplayRole).strip()
            encrypt_type = selected_item[0].parent().data(Qt.ItemDataRole.DisplayRole).strip()   # Passphrase Encrypted / Public Key Encrypted

            reply = QMessageBox.question(self, 
                                     'System Prompt', 
                                     '<html><head/><body><p><span style=\" font-size:15pt;\">Are you sure you want to delete the file?</span></p></body></html>' 
                                     f'<html><head/><body><p><span style=\" font-size:13pt; font-weight:bold;\">{filename}</span></p></body></html>', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                if encrypt_type == 'Passphrase Encrypted':
                    file_path = os.path.join(self.users_path, self.user.username, 'passEncrypt', f"{filename}.bin")
                    if file_path:
                        if os.path.exists(file_path):
                            os.remove(file_path)
                            self.initialFileList()
                elif encrypt_type == 'Public Key Encrypted':
                    file_path = os.path.join(self.users_path, self.user.username, 'keyEncrypt', 'files', f"{filename}.bin")
                    fileKey_path = os.path.join(self.users_path, self.user.username, 'keyEncrypt', 'keys', f"{filename}.bin")
                    if file_path and fileKey_path:
                        if os.path.exists(file_path) and os.path.exists(fileKey_path):
                            os.remove(file_path)
                            os.remove(fileKey_path)
                            self.initialFileList()

    def get_privateKey_file(self):
        self.private_key_file = self.upload_privateKey_window.file_path

    def download_decrypt_file(self):
        selected_item = self.treeView.selectedIndexes()
        # check if user have selected any item AND it's a file item
        if selected_item and selected_item[0].parent().data(Qt.ItemDataRole.DisplayRole) != None:
            self.toBeDecryptFile = selected_item[0].data(Qt.ItemDataRole.DisplayRole).strip()
            encrypt_type = selected_item[0].parent().data(Qt.ItemDataRole.DisplayRole).strip()   # Passphrase Encrypted / Public Key Encrypted
                
            if encrypt_type == 'Passphrase Encrypted':
                # open download file window
                self.download_decrypted_file_window = DownloadDecryptedFile.Ui_Form()
                self.download_decrypted_file_window.users_path = self.users_path
                self.download_decrypted_file_window.user = self.user
                self.download_decrypted_file_window.filename = self.toBeDecryptFile
                self.download_decrypted_file_window.encrypt_type = encrypt_type
                self.download_decrypted_file_window.show()
            elif encrypt_type == 'Public Key Encrypted':
                # Check if user give the private key file path or not
                validPrivateKey = False
                if self.private_key_file != None and os.path.isfile(self.private_key_file):
                    if os.path.splitext(os.path.basename(self.private_key_file))[1] == '.pem':
                        try:
                            with open(self.private_key_file, 'rb') as file:
                                private_key = serialization.load_pem_private_key(
                                    file.read(),
                                    password=self.user.pwd.encode(),
                                    backend=default_backend()
                                )
                        except:
                            pass
                        else:
                            validPrivateKey = True

                if not validPrivateKey:     # Not given valid private key
                    # Open the upload private key window
                    self.upload_privateKey_window = UploadPrivateKey.Ui_Form()
                    self.upload_privateKey_window.user = self.user
                    self.upload_privateKey_window.show()
                    self.upload_privateKey_window.privateKey_uploaded.connect(self.get_privateKey_file)
                    self.upload_privateKey_window.privateKey_uploaded.connect(self.upload_privateKey_window.hide)
                    self.upload_privateKey_window.privateKey_uploaded.connect(self.download_decrypt_file_pubKey)
                else:                       # Given valid private key
                    # open download file window
                    self.download_decrypt_file_pubKey()

    def download_decrypt_file_pubKey(self):
        # open download file window
        self.download_decrypted_file_window = DownloadDecryptedFile.Ui_Form()
        self.download_decrypted_file_window.users_path = self.users_path
        self.download_decrypted_file_window.user = self.user
        self.download_decrypted_file_window.filename = self.toBeDecryptFile
        self.download_decrypted_file_window.encrypt_type = 'Public Key Encrypted'
        self.download_decrypted_file_window.private_key_file = self.private_key_file
        self.download_decrypted_file_window.mainWindow_self = self
        self.download_decrypted_file_window.show()


    def initialFileList(self):
        #* For password encrypt
        passEncypt_path = os.path.join(self.users_path, self.user.username, 'passEncrypt')
        pass_files_ls = Prog_FileManage.get_file_items_list(passEncypt_path)
        if len(pass_files_ls) != 0:
            # Remove existing child rows from self.fileType1
            self.fileType1.removeRows(0, self.fileType1.rowCount())
            for file in pass_files_ls:
                self.fileType1.appendRow(file)
        else:
            self.fileType1.removeRows(0, self.fileType1.rowCount())

        #* For pubKey encrypt
        keyEncypt_path = os.path.join(self.users_path, self.user.username, 'keyEncrypt', 'files')
        key_files_ls = Prog_FileManage.get_file_items_list(keyEncypt_path)
        if len(key_files_ls) != 0:
            self.fileType2.removeRows(0, self.fileType2.rowCount())
            for file in key_files_ls:
                self.fileType2.appendRow(file)
        else:
            self.fileType2.removeRows(0, self.fileType2.rowCount())
            

    def encryption(self):
        self.encryption_window = Encryption.Ui_Form()
        self.encryption_window.show()


    def keyGeneration(self):
        self.keyGeneration_window = KeyGeneration.Ui_Form()
        self.keyGeneration_window.show()


    def logout(self):
        reply = QMessageBox.question(self, 
                                     'System Prompt', 
                                     '<html><head/><body><p><span style=\" font-size:13pt;\">Do you want to logout?</span></p></body></html>', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.user.empty()
            self.close()

    # do cleanup if the user close the main window
    def closeEvent(self, event):
        self.user.empty()
        # Allow the window to close
        event.accept()


# if __name__ == '__main__':
#     try:
#         app = QApplication(sys.argv)
#         main = Ui_MainWindow()

        

#         main.show()
#         sys.exit(app.exec())
#     except Exception as e:
#         print(e)