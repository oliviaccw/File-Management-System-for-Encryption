from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox
import sys, os

import Encrypt as Prog_Encrypt


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.tab1_output_folder_path = None
        self.tab2_output_folder_path = None
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(668, 387)
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 641, 361))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.public_key_generation = QtWidgets.QWidget()
        self.public_key_generation.setObjectName("public_key_generation")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.public_key_generation)
        self.groupBox_5.setGeometry(QtCore.QRect(60, 170, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setFlat(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.layoutWidget_5 = QtWidgets.QWidget(parent=self.groupBox_5)
        self.layoutWidget_5.setGeometry(QtCore.QRect(0, 30, 431, 30))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tab1_select_folder_input = QtWidgets.QLineEdit(parent=self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_select_folder_input.sizePolicy().hasHeightForWidth())
        self.tab1_select_folder_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab1_select_folder_input.setFont(font)
        self.tab1_select_folder_input.setReadOnly(True)
        self.tab1_select_folder_input.setObjectName("tab1_select_folder_input")
        self.horizontalLayout_5.addWidget(self.tab1_select_folder_input)
        self.tab1_select_folder_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_select_folder_Btn.sizePolicy().hasHeightForWidth())
        self.tab1_select_folder_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab1_select_folder_Btn.setFont(font)
        self.tab1_select_folder_Btn.setObjectName("tab1_select_folder_Btn")

        #? signal for tab1 output file select folder btn
        self.tab1_select_folder_Btn.clicked.connect(self.tab1_select_folder)

        self.horizontalLayout_5.addWidget(self.tab1_select_folder_Btn)
        self.tab1_generate_Btn = QtWidgets.QPushButton(parent=self.public_key_generation)
        self.tab1_generate_Btn.setGeometry(QtCore.QRect(180, 270, 261, 28))
        self.tab1_generate_Btn.setObjectName("tab1_generate_Btn")

        #? signal for tab1 output file select folder btn
        self.tab1_generate_Btn.clicked.connect(self.tab1_generation)

        self.groupBox = QtWidgets.QGroupBox(parent=self.public_key_generation)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 611, 131))
        self.groupBox.setObjectName("groupBox")
        self.label_signal = QtWidgets.QLabel(parent=self.groupBox)
        self.label_signal.setGeometry(QtCore.QRect(20, 20, 571, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_signal.sizePolicy().hasHeightForWidth())
        self.label_signal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        self.label_signal.setFont(font)
        self.label_signal.setStyleSheet(" ;")
        self.label_signal.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_signal.setWordWrap(True)
        self.label_signal.setObjectName("label_signal")
        self.tabWidget.addTab(self.public_key_generation, "")
        self.symmetric_key_generation = QtWidgets.QWidget()
        self.symmetric_key_generation.setObjectName("symmetric_key_generation")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.symmetric_key_generation)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 30, 591, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_signal_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_signal_2.setGeometry(QtCore.QRect(20, 30, 571, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_signal_2.sizePolicy().hasHeightForWidth())
        self.label_signal_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        self.label_signal_2.setFont(font)
        self.label_signal_2.setStyleSheet("")
        self.label_signal_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_signal_2.setWordWrap(True)
        self.label_signal_2.setObjectName("label_signal_2")
        self.groupBox_9 = QtWidgets.QGroupBox(parent=self.symmetric_key_generation)
        self.groupBox_9.setGeometry(QtCore.QRect(50, 160, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setFlat(True)
        self.groupBox_9.setObjectName("groupBox_9")
        self.layoutWidget_9 = QtWidgets.QWidget(parent=self.groupBox_9)
        self.layoutWidget_9.setGeometry(QtCore.QRect(0, 30, 431, 30))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.symmetric_key_output_folder_input = QtWidgets.QLineEdit(parent=self.layoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.symmetric_key_output_folder_input.sizePolicy().hasHeightForWidth())
        self.symmetric_key_output_folder_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.symmetric_key_output_folder_input.setFont(font)
        self.symmetric_key_output_folder_input.setReadOnly(True)
        self.symmetric_key_output_folder_input.setObjectName("symmetric_key_output_folder_input")
        self.horizontalLayout_9.addWidget(self.symmetric_key_output_folder_input)
        self.symmetric_key_select_folder_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.symmetric_key_select_folder_Btn.sizePolicy().hasHeightForWidth())
        self.symmetric_key_select_folder_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.symmetric_key_select_folder_Btn.setFont(font)
        self.symmetric_key_select_folder_Btn.setObjectName("symmetric_key_select_folder_Btn")

        #? signal for tab1 output file select folder btn
        self.symmetric_key_select_folder_Btn.clicked.connect(self.tab2_select_folder)

        self.horizontalLayout_9.addWidget(self.symmetric_key_select_folder_Btn)
        self.tab2_generate_Btn = QtWidgets.QPushButton(parent=self.symmetric_key_generation)
        self.tab2_generate_Btn.setGeometry(QtCore.QRect(170, 250, 261, 28))
        self.tab2_generate_Btn.setObjectName("tab2_generate_Btn")

        #? signal for tab2 generate btn
        self.tab2_generate_Btn.clicked.connect(self.tab2_generation)

        self.tabWidget.addTab(self.symmetric_key_generation, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Key Generation"))
        self.tabWidget.setToolTip(_translate("Form", "<html><head/><body><p>Public Key Generation</p></body></html>"))
        self.groupBox_5.setTitle(_translate("Form", "Output Folder"))
        self.tab1_select_folder_Btn.setText(_translate("Form", "Choose a folder"))
        self.tab1_generate_Btn.setText(_translate("Form", "Generate"))
        self.groupBox.setTitle(_translate("Form", "Information"))
        self.label_signal.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Private key &amp; Public key</span><span style=\" font-size:9pt;\">: 2048 bits key (work with RSA)</span></p><p><span style=\" font-size:9pt; font-weight:600;\">Encrypted Symmetric Key</span><span style=\" font-size:9pt;\">: 256 bits key (encrypted by the generated public key)</span></p><p><span style=\" font-size:9pt; font-weight:600; color:#0000ff;\">Please choose a folder to save the key files.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.public_key_generation), _translate("Form", "Public Key Generation"))
        self.groupBox_2.setTitle(_translate("Form", "Information"))
        self.label_signal_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Symmetric Key</span>: 256 bits key</p><p><span style=\" font-weight:600; color:#0000ff;\">Please choose a folder to save the key file.</span></p></body></html>"))
        self.groupBox_9.setTitle(_translate("Form", "Symmetric Key Output Folder"))
        self.symmetric_key_select_folder_Btn.setText(_translate("Form", "Choose a folder"))
        self.tab2_generate_Btn.setText(_translate("Form", "Generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.symmetric_key_generation), _translate("Form", "Symmetric Key Generation"))


    
    def tab1_select_folder(self):
        self.tab1_output_folder_path = QFileDialog().getExistingDirectory(self, "Select Directory", "C:\\")
        self.tab1_select_folder_input.setText(self.tab1_output_folder_path)
    
    def tab2_select_folder(self):
        self.tab2_output_folder_path = QFileDialog().getExistingDirectory(self, "Select Directory", "C:\\")
        self.symmetric_key_output_folder_input.setText(self.tab2_output_folder_path)

    def tab1_generation(self):
        if self.tab1_output_folder_path == None:
            QMessageBox.warning(None, 
                             'Not Complete', 
                             '<html><head/><body><p><span style=\" font-size:15pt;\">Not Complete</span></p></body></html>'
                             '<html><head/><body><p><span style=\" font-size:11pt;\">Please choose a folder first.</span></p></body></html>',
                             QMessageBox.StandardButton.Ok, 
                             QMessageBox.StandardButton.Ok)
        else:
            private_key_filename = self.check_file_duplicate('private_key.pem', self.tab1_output_folder_path)
            public_key_filename = self.check_file_duplicate('public_key.pem', self.tab1_output_folder_path)
            encrypted_symmetric_key_filename = self.check_file_duplicate('encrypted_symmetric_key.bin', self.tab1_output_folder_path)
            
            private_key_file = os.path.join(self.tab1_output_folder_path, private_key_filename)
            public_key_file = os.path.join(self.tab1_output_folder_path, public_key_filename)
            encrypted_symmetric_key_file = os.path.join(self.tab1_output_folder_path, encrypted_symmetric_key_filename)
            
            private_key, public_key = Prog_Encrypt.generate_key_pair()
            Prog_Encrypt.save_private_key_without_pwd(private_key, private_key_file)
            Prog_Encrypt.save_public_key(public_key, public_key_file)
            Prog_Encrypt.generate_and_save_encrypted_symmetric_key(public_key, encrypted_symmetric_key_file)

            while not os.path.isfile(private_key_file) or not os.path.isfile(public_key_file) or not os.path.isfile(encrypted_symmetric_key_file):
                continue
            QMessageBox.information(None, 
                                    'File Management System', 
                                    '<html><head/><body><p><span style=\" font-size:15pt;\">Keys generated successfully</span></p></body></html>'
                                    f'<html><head/><body><p><span style=\" font-size:11pt;\">{private_key_filename}</span></p></body></html>'
                                    f'<html><head/><body><p><span style=\" font-size:11pt;\">{public_key_filename}</span></p></body></html>'
                                    f'<html><head/><body><p><span style=\" font-size:11pt;\">{encrypted_symmetric_key_filename}</span></p></body></html>', 
                                    QMessageBox.StandardButton.Ok, 
                                    QMessageBox.StandardButton.Ok)


    def tab2_generation(self):
        if self.tab2_output_folder_path == None:
            QMessageBox.warning(None, 
                             'File Management System', 
                             '<html><head/><body><p><span style=\" font-size:15pt;\">Not Complete</span></p></body></html>'
                             '<html><head/><body><p><span style=\" font-size:11pt;\">Please choose a folder first.</span></p></body></html>',
                             QMessageBox.StandardButton.Ok, 
                             QMessageBox.StandardButton.Ok)
        else:
            filename = self.check_file_duplicate('symmetric_key.bin', self.tab2_output_folder_path)
            symmetric_key_file = os.path.join(self.tab2_output_folder_path, filename)
            Prog_Encrypt.generate_and_save_symmetric_key(symmetric_key_file)

            while not os.path.isfile(symmetric_key_file):
                continue
            QMessageBox.information(None, 
                                    'File Management System', 
                                    '<html><head/><body><p><span style=\" font-size:15pt;\">Key generated successfully</span></p></body></html>'
                                    f'<html><head/><body><p><span style=\" font-size:11pt;\">{filename}</span></p></body></html>',
                                    QMessageBox.StandardButton.Ok, 
                                    QMessageBox.StandardButton.Ok)
            
    # check if have duplicated file in the destination path
    def check_file_duplicate(self, filename, folder_path):
        isDuplicate = True
        base_name, ext = os.path.splitext(filename)
        count = 0
        while isDuplicate:
            isDuplicate = False
            for check_filename in os.listdir(folder_path):
                if check_filename == filename:
                    isDuplicate = True
                    count += 1
                    filename = f"{base_name} ({count}){ext}"
                    break
        return filename
    
    
