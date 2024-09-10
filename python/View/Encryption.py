from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QFileDialog, QApplication, QMessageBox
import sys, os

import Encrypt as Prog_Encrypt


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setWindowFlag(QtCore.Qt.WindowType.MSWindowsFixedSizeDialogHint)
        self.tab1_input_file_path = None
        self.tab1_output_file_path = None

        self.tab2_input_file_path = None
        self.tab2_output_folder_path = None
        self.tab2_private_key_file_path = None
        self.tab2_encrypted_symmetri_key_file_path = None

        self.tab3_input_file_path = None
        self.tab3_output_folder_path = None
        self.tab3_private_key_file_path = None
        self.tab3_public_key_file_path = None

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(563, 551)
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 551, 541))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.PreventContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setElideMode(QtCore.Qt.TextElideMode.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")
        self.passphrase_encryption_tab = QtWidgets.QWidget()
        self.passphrase_encryption_tab.setObjectName("passphrase_encryption_tab")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.passphrase_encryption_tab)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 20, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget_3 = QtWidgets.QWidget(parent=self.groupBox_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 30, 431, 30))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tab1_input_file = QtWidgets.QLineEdit(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_input_file.sizePolicy().hasHeightForWidth())
        self.tab1_input_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab1_input_file.setFont(font)
        self.tab1_input_file.setReadOnly(True)
        self.tab1_input_file.setObjectName("tab1_input_file")
        self.horizontalLayout_2.addWidget(self.tab1_input_file)
        self.tab1_input_file_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_input_file_Btn.sizePolicy().hasHeightForWidth())
        self.tab1_input_file_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab1_input_file_Btn.setFont(font)
        self.tab1_input_file_Btn.setObjectName("tab1_input_file_Btn")

        #? signal for tab1 input file select btn
        self.tab1_input_file_Btn.clicked.connect(self.tab1_select_input_file)

        self.horizontalLayout_2.addWidget(self.tab1_input_file_Btn)
        self.label_3 = QtWidgets.QLabel(parent=self.passphrase_encryption_tab)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 121, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.tab1_input_pwd = QtWidgets.QLineEdit(parent=self.passphrase_encryption_tab)
        self.tab1_input_pwd.setGeometry(QtCore.QRect(20, 210, 431, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_input_pwd.sizePolicy().hasHeightForWidth())
        self.tab1_input_pwd.setSizePolicy(sizePolicy)
        self.tab1_input_pwd.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tab1_input_pwd.setFont(font)
        self.tab1_input_pwd.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.tab1_input_pwd.setObjectName("tab1_input_pwd")
        self.groupBox = QtWidgets.QGroupBox(parent=self.passphrase_encryption_tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 270, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setUnderline(False)
        self.groupBox.setFont(font)
        self.groupBox.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 20, 461, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab1_encrypt_Btn = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tab1_encrypt_Btn.setFont(font)
        self.tab1_encrypt_Btn.setObjectName("tab1_encrypt_Btn")
        self.horizontalLayout.addWidget(self.tab1_encrypt_Btn)
        self.tab1_decrypt_Btn = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tab1_decrypt_Btn.setFont(font)
        self.tab1_decrypt_Btn.setObjectName("tab1_decrypt_Btn")
        self.horizontalLayout.addWidget(self.tab1_decrypt_Btn)
        self.tab1_confirm_Btn = QtWidgets.QPushButton(parent=self.passphrase_encryption_tab)
        self.tab1_confirm_Btn.setGeometry(QtCore.QRect(130, 390, 261, 28))
        self.tab1_confirm_Btn.setObjectName("tab1_confirm_Btn")

        #? signal for tab1 input file select btn
        self.tab1_confirm_Btn.clicked.connect(self.tab1_confirm)

        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.passphrase_encryption_tab)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 100, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget_4 = QtWidgets.QWidget(parent=self.groupBox_3)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 30, 431, 30))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tab1_output_file = QtWidgets.QLineEdit(parent=self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_output_file.sizePolicy().hasHeightForWidth())
        self.tab1_output_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab1_output_file.setFont(font)
        self.tab1_output_file.setReadOnly(True)
        self.tab1_output_file.setObjectName("tab1_output_file")
        self.horizontalLayout_4.addWidget(self.tab1_output_file)
        self.tab1_output_file_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_output_file_Btn.sizePolicy().hasHeightForWidth())
        self.tab1_output_file_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab1_output_file_Btn.setFont(font)
        self.tab1_output_file_Btn.setObjectName("tab1_output_file_Btn")

        #? signal for tab1 input file select btn
        self.tab1_output_file_Btn.clicked.connect(self.tab1_select_output_file)

        self.horizontalLayout_4.addWidget(self.tab1_output_file_Btn)
        self.tabWidget.addTab(self.passphrase_encryption_tab, "")
        self.public_key_encryption = QtWidgets.QWidget()
        self.public_key_encryption.setObjectName("public_key_encryption")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.public_key_encryption)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 340, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setUnderline(False)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.groupBox_4)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(60, 20, 461, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tab2_encrypt_Btn = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tab2_encrypt_Btn.setFont(font)
        self.tab2_encrypt_Btn.setObjectName("tab2_encrypt_Btn")
        self.horizontalLayout_3.addWidget(self.tab2_encrypt_Btn)
        self.tab2_decrypt_Btn = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tab2_decrypt_Btn.setFont(font)
        self.tab2_decrypt_Btn.setObjectName("tab2_decrypt_Btn")
        self.horizontalLayout_3.addWidget(self.tab2_decrypt_Btn)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.public_key_encryption)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 20, 521, 81))
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
        self.tab2_input_file = QtWidgets.QLineEdit(parent=self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab2_input_file.sizePolicy().hasHeightForWidth())
        self.tab2_input_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab2_input_file.setFont(font)
        self.tab2_input_file.setReadOnly(True)
        self.tab2_input_file.setObjectName("tab2_input_file")
        self.horizontalLayout_5.addWidget(self.tab2_input_file)
        self.tab2_input_file_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab2_input_file_Btn.sizePolicy().hasHeightForWidth())
        self.tab2_input_file_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab2_input_file_Btn.setFont(font)
        self.tab2_input_file_Btn.setObjectName("tab2_input_file_Btn")

        #? signal for tab2 input file select btn
        self.tab2_input_file_Btn.clicked.connect(self.tab2_select_input_file)

        self.horizontalLayout_5.addWidget(self.tab2_input_file_Btn)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.public_key_encryption)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 100, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setFlat(True)
        self.groupBox_6.setObjectName("groupBox_6")
        self.layoutWidget_6 = QtWidgets.QWidget(parent=self.groupBox_6)
        self.layoutWidget_6.setGeometry(QtCore.QRect(0, 30, 431, 30))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tab2_output_file = QtWidgets.QLineEdit(parent=self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab2_output_file.sizePolicy().hasHeightForWidth())
        self.tab2_output_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab2_output_file.setFont(font)
        self.tab2_output_file.setReadOnly(True)
        self.tab2_output_file.setObjectName("tab2_output_file")
        self.horizontalLayout_6.addWidget(self.tab2_output_file)
        self.tab2_output_file_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab2_output_file_Btn.sizePolicy().hasHeightForWidth())
        self.tab2_output_file_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab2_output_file_Btn.setFont(font)
        self.tab2_output_file_Btn.setObjectName("tab2_output_file_Btn")

        #? signal for tab2 output file select btn
        self.tab2_output_file_Btn.clicked.connect(self.tab2_select_output_folder)

        self.horizontalLayout_6.addWidget(self.tab2_output_file_Btn)
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.public_key_encryption)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 180, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setFlat(True)
        self.groupBox_7.setObjectName("groupBox_7")
        self.layoutWidget_7 = QtWidgets.QWidget(parent=self.groupBox_7)
        self.layoutWidget_7.setGeometry(QtCore.QRect(0, 30, 431, 30))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tab2_private_key_file = QtWidgets.QLineEdit(parent=self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab2_private_key_file.sizePolicy().hasHeightForWidth())
        self.tab2_private_key_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab2_private_key_file.setFont(font)
        self.tab2_private_key_file.setReadOnly(True)
        self.tab2_private_key_file.setObjectName("tab2_private_key_file")
        self.horizontalLayout_7.addWidget(self.tab2_private_key_file)
        self.tab2_private_key_file_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab2_private_key_file_Btn.sizePolicy().hasHeightForWidth())
        self.tab2_private_key_file_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab2_private_key_file_Btn.setFont(font)
        self.tab2_private_key_file_Btn.setObjectName("tab2_private_key_file_Btn")

        #? signal for tab2 private key file select btn
        self.tab2_private_key_file_Btn.clicked.connect(self.tab2_select_private_key_file)

        self.horizontalLayout_7.addWidget(self.tab2_private_key_file_Btn)
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.public_key_encryption)
        self.groupBox_8.setGeometry(QtCore.QRect(20, 260, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setFlat(True)
        self.groupBox_8.setObjectName("groupBox_8")
        self.layoutWidget_8 = QtWidgets.QWidget(parent=self.groupBox_8)
        self.layoutWidget_8.setGeometry(QtCore.QRect(0, 30, 431, 30))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tab2_encrypted_symmetri_key_file = QtWidgets.QLineEdit(parent=self.layoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab2_encrypted_symmetri_key_file.sizePolicy().hasHeightForWidth())
        self.tab2_encrypted_symmetri_key_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab2_encrypted_symmetri_key_file.setFont(font)
        self.tab2_encrypted_symmetri_key_file.setReadOnly(True)
        self.tab2_encrypted_symmetri_key_file.setObjectName("tab2_encrypted_symmetri_key_file")
        self.horizontalLayout_8.addWidget(self.tab2_encrypted_symmetri_key_file)
        self.tab2_encrypted_symmetri_key_file_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab2_encrypted_symmetri_key_file_Btn.sizePolicy().hasHeightForWidth())
        self.tab2_encrypted_symmetri_key_file_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab2_encrypted_symmetri_key_file_Btn.setFont(font)
        self.tab2_encrypted_symmetri_key_file_Btn.setObjectName("tab2_encrypted_symmetri_key_file_Btn")

        #? signal for tab2 encrypted symmetric key file select btn
        self.tab2_encrypted_symmetri_key_file_Btn.clicked.connect(self.tab2_select_encrypted_symmetric_key_file)

        self.horizontalLayout_8.addWidget(self.tab2_encrypted_symmetri_key_file_Btn)
        self.tab2_confirm_Btn = QtWidgets.QPushButton(parent=self.public_key_encryption)
        self.tab2_confirm_Btn.setGeometry(QtCore.QRect(140, 450, 261, 28))
        self.tab2_confirm_Btn.setObjectName("tab2_confirm_Btn")

        #? signal for tab2 confirm btn
        self.tab2_confirm_Btn.clicked.connect(self.tab2_confirm)
        
        self.tabWidget.addTab(self.public_key_encryption, "")
        self.public_key_encryption_rsa = QtWidgets.QWidget()
        self.public_key_encryption_rsa.setObjectName("public_key_encryption_rsa")
        self.groupBox_9 = QtWidgets.QGroupBox(parent=self.public_key_encryption_rsa)
        self.groupBox_9.setGeometry(QtCore.QRect(20, 20, 521, 81))
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
        self.tab3_input_file = QtWidgets.QLineEdit(parent=self.layoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab3_input_file.sizePolicy().hasHeightForWidth())
        self.tab3_input_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab3_input_file.setFont(font)
        self.tab3_input_file.setText("")
        self.tab3_input_file.setReadOnly(True)
        self.tab3_input_file.setObjectName("tab3_input_file")
        self.horizontalLayout_9.addWidget(self.tab3_input_file)
        self.tab3_input_file_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab3_input_file_Btn.sizePolicy().hasHeightForWidth())
        self.tab3_input_file_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab3_input_file_Btn.setFont(font)
        self.tab3_input_file_Btn.setObjectName("tab3_input_file_Btn")

        #? signal for tab3 input file select btn
        self.tab3_input_file_Btn.clicked.connect(self.tab3_select_input_file)

        self.horizontalLayout_9.addWidget(self.tab3_input_file_Btn)
        self.groupBox_10 = QtWidgets.QGroupBox(parent=self.public_key_encryption_rsa)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 100, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setFlat(True)
        self.groupBox_10.setObjectName("groupBox_10")
        self.layoutWidget_10 = QtWidgets.QWidget(parent=self.groupBox_10)
        self.layoutWidget_10.setGeometry(QtCore.QRect(0, 30, 431, 30))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tab3_output_file = QtWidgets.QLineEdit(parent=self.layoutWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab3_output_file.sizePolicy().hasHeightForWidth())
        self.tab3_output_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab3_output_file.setFont(font)
        self.tab3_output_file.setReadOnly(True)
        self.tab3_output_file.setObjectName("tab3_output_file")
        self.horizontalLayout_10.addWidget(self.tab3_output_file)
        self.tab3_output_file_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab3_output_file_Btn.sizePolicy().hasHeightForWidth())
        self.tab3_output_file_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab3_output_file_Btn.setFont(font)
        self.tab3_output_file_Btn.setObjectName("tab3_output_file_Btn")

        #? signal for tab3 output folder select btn
        self.tab3_output_file_Btn.clicked.connect(self.tab3_select_output_folder)

        self.horizontalLayout_10.addWidget(self.tab3_output_file_Btn)
        self.groupBox_11 = QtWidgets.QGroupBox(parent=self.public_key_encryption_rsa)
        self.groupBox_11.setGeometry(QtCore.QRect(20, 180, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setFlat(True)
        self.groupBox_11.setObjectName("groupBox_11")
        self.layoutWidget_11 = QtWidgets.QWidget(parent=self.groupBox_11)
        self.layoutWidget_11.setGeometry(QtCore.QRect(0, 30, 431, 30))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tab3_private_key_file = QtWidgets.QLineEdit(parent=self.layoutWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab3_private_key_file.sizePolicy().hasHeightForWidth())
        self.tab3_private_key_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab3_private_key_file.setFont(font)
        self.tab3_private_key_file.setReadOnly(True)
        self.tab3_private_key_file.setObjectName("tab3_private_key_file")
        self.horizontalLayout_11.addWidget(self.tab3_private_key_file)
        self.tab3_private_key_file_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab3_private_key_file_Btn.sizePolicy().hasHeightForWidth())
        self.tab3_private_key_file_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab3_private_key_file_Btn.setFont(font)
        self.tab3_private_key_file_Btn.setObjectName("tab3_private_key_file_Btn")

        #? signal for tab3 private key file select btn
        self.tab3_private_key_file_Btn.clicked.connect(self.tab3_select_private_key_file)

        self.horizontalLayout_11.addWidget(self.tab3_private_key_file_Btn)
        self.groupBox_12 = QtWidgets.QGroupBox(parent=self.public_key_encryption_rsa)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 260, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setFlat(True)
        self.groupBox_12.setObjectName("groupBox_12")
        self.layoutWidget_12 = QtWidgets.QWidget(parent=self.groupBox_12)
        self.layoutWidget_12.setGeometry(QtCore.QRect(0, 30, 431, 30))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.tab3_public_key_file = QtWidgets.QLineEdit(parent=self.layoutWidget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab3_public_key_file.sizePolicy().hasHeightForWidth())
        self.tab3_public_key_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab3_public_key_file.setFont(font)
        self.tab3_public_key_file.setReadOnly(True)
        self.tab3_public_key_file.setObjectName("tab3_public_key_file")
        self.horizontalLayout_12.addWidget(self.tab3_public_key_file)
        self.tab3_public_key_file_Btn = QtWidgets.QPushButton(parent=self.layoutWidget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab3_public_key_file_Btn.sizePolicy().hasHeightForWidth())
        self.tab3_public_key_file_Btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.tab3_public_key_file_Btn.setFont(font)
        self.tab3_public_key_file_Btn.setObjectName("tab3_public_key_file_Btn")

        #? signal for tab3 public key file select btn
        self.tab3_public_key_file_Btn.clicked.connect(self.tab3_select_public_key_file)

        self.horizontalLayout_12.addWidget(self.tab3_public_key_file_Btn)
        self.groupBox_13 = QtWidgets.QGroupBox(parent=self.public_key_encryption_rsa)
        self.groupBox_13.setGeometry(QtCore.QRect(20, 340, 521, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setUnderline(False)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.groupBox_13.setFlat(False)
        self.groupBox_13.setCheckable(False)
        self.groupBox_13.setObjectName("groupBox_13")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.groupBox_13)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(60, 20, 461, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.tab3_encrypt_Btn = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tab3_encrypt_Btn.setFont(font)
        self.tab3_encrypt_Btn.setObjectName("tab3_encrypt_Btn")
        self.horizontalLayout_13.addWidget(self.tab3_encrypt_Btn)
        self.tab3_decrypt_Btn = QtWidgets.QRadioButton(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tab3_decrypt_Btn.setFont(font)
        self.tab3_decrypt_Btn.setObjectName("tab3_decrypt_Btn")
        self.horizontalLayout_13.addWidget(self.tab3_decrypt_Btn)
        self.tab3_confirm_Btn = QtWidgets.QPushButton(parent=self.public_key_encryption_rsa)
        self.tab3_confirm_Btn.setGeometry(QtCore.QRect(140, 450, 261, 28))
        self.tab3_confirm_Btn.setObjectName("tab3_confirm_Btn")

        #? signal for tab3 confirm btn
        self.tab3_confirm_Btn.clicked.connect(self.tab3_confirm)

        self.tabWidget.addTab(self.public_key_encryption_rsa, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Encryption"))
        self.groupBox_2.setTitle(_translate("Form", "Input File"))
        self.tab1_input_file_Btn.setText(_translate("Form", "Choose a file"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">Passphrase: </span></p></body></html>"))
        self.tab1_input_pwd.setPlaceholderText(_translate("Form", "Enter your passphrase"))
        self.groupBox.setTitle(_translate("Form", "Operation"))
        self.tab1_encrypt_Btn.setText(_translate("Form", "Encryption"))
        self.tab1_decrypt_Btn.setText(_translate("Form", "Decryption"))
        self.tab1_confirm_Btn.setText(_translate("Form", "Confirm"))
        self.groupBox_3.setTitle(_translate("Form", "Output Folder"))
        self.tab1_output_file_Btn.setText(_translate("Form", "Choose a folder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.passphrase_encryption_tab), _translate("Form", "Passphrase Encryption"))
        self.groupBox_4.setTitle(_translate("Form", "Operation"))
        self.tab2_encrypt_Btn.setText(_translate("Form", "Encryption"))
        self.tab2_decrypt_Btn.setText(_translate("Form", "Decryption"))
        self.groupBox_5.setTitle(_translate("Form", "Input File"))
        self.tab2_input_file_Btn.setText(_translate("Form", "Choose a file"))
        self.groupBox_6.setTitle(_translate("Form", "Output Folder"))
        self.tab2_output_file_Btn.setText(_translate("Form", "Choose a folder"))
        self.groupBox_7.setTitle(_translate("Form", "Private Key File"))
        self.tab2_private_key_file_Btn.setText(_translate("Form", "Choose a file"))
        self.groupBox_8.setTitle(_translate("Form", "Encrypted Symmetric Key File"))
        self.tab2_encrypted_symmetri_key_file_Btn.setText(_translate("Form", "Choose a file"))
        self.tab2_confirm_Btn.setText(_translate("Form", "Confirm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.public_key_encryption), _translate("Form", "Public Key Encryption(with AES)"))
        self.groupBox_9.setTitle(_translate("Form", "Input File"))
        self.tab3_input_file_Btn.setText(_translate("Form", "Choose a file"))
        self.groupBox_10.setTitle(_translate("Form", "Output Folder"))
        self.tab3_output_file_Btn.setText(_translate("Form", "Choose a folder"))
        self.groupBox_11.setTitle(_translate("Form", "Private Key File"))
        self.tab3_private_key_file_Btn.setText(_translate("Form", "Choose a file"))
        self.groupBox_12.setTitle(_translate("Form", "Public Key File"))
        self.tab3_public_key_file_Btn.setText(_translate("Form", "Choose a file"))
        self.groupBox_13.setTitle(_translate("Form", "Operation"))
        self.tab3_encrypt_Btn.setText(_translate("Form", "Encryption"))
        self.tab3_decrypt_Btn.setText(_translate("Form", "Decryption"))
        self.tab3_confirm_Btn.setText(_translate("Form", "Confirm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.public_key_encryption_rsa), _translate("Form", "Public Key Encryption(RSA)"))

    #* Tab 1 Passphrase Encryption
    def tab1_select_input_file(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFile)
        fd.setDirectory('C:\\')
        if fd.exec():
            self.tab1_input_file_path = fd.selectedFiles()[0]
            self.tab1_input_file.setText(self.tab1_input_file_path)

    def tab1_select_output_file(self):
        self.tab1_output_file_path = QFileDialog().getExistingDirectory(self, "Select Directory", "C:\\")
        self.tab1_output_file.setText(self.tab1_output_file_path)

    def tab1_confirm(self):
        isInput = False
        isOutput = False
        isPwd = False 
        isChoice = False
        if self.tab1_input_file_path != None:
            isInput = True
        if self.tab1_output_file_path != None:
            isOutput = True
        if self.tab1_input_pwd.text().strip != None:
            isPwd = True
        if self.tab1_encrypt_Btn.isChecked() or self.tab1_decrypt_Btn.isChecked():
            isChoice = True

        if isInput and isOutput and isPwd and isChoice:
            if self.tab1_encrypt_Btn.isChecked():   # perform encryption
                filename = os.path.basename(self.tab1_input_file_path)
                filename = self.check_file_duplicate_with_bin(f'encrypted_{filename}', self.tab1_output_file_path)
                output_filename = f'{filename}.bin'
                output_file = os.path.join(self.tab1_output_file_path, output_filename)
                Prog_Encrypt.encrypt_file_with_pwd(self.tab1_input_file_path, output_file, self.tab1_input_pwd.text().strip())

                while not os.path.isfile(output_file):
                    continue
                self.show_success('Finish File Encryption', output_filename)
            else:   # perform decryption
                filename = os.path.splitext(os.path.basename(self.tab1_input_file_path))[0]     # assume filename has 2 file extention (e.g. test.pdf.bin)
                filename, ext = os.path.splitext(filename)
                if ext == '': # input file only have 1 extention -> give .bin as ext
                    filename = f'{filename}.bin'
                else:
                    filename = filename + ext
                filename = self.check_file_duplicate(f'decrypted_{filename}', self.tab1_output_file_path)
                output_file = os.path.join(self.tab1_output_file_path, filename)
                try:
                    Prog_Encrypt.decrypt_file_with_pwd(self.tab1_input_file_path, output_file, self.tab1_input_pwd.text().strip())
                except:
                    QMessageBox.warning(None, 
                             'File Management System', 
                             '<html><head/><body><p><span style=\" font-size:15pt;\">Fail to Decrypt</span></p></body></html>'
                             '<html><head/><body><p><span style=\" font-size:11pt;\">Wrong input file or passphrase</span></p></body></html>',
                             QMessageBox.StandardButton.Ok, 
                             QMessageBox.StandardButton.Ok)
                else:
                    while not os.path.isfile(output_file):
                        continue
                    self.show_success('Finish File Decryption', filename)

        else:   # not fill in all the option
            self.show_not_complete_warning()
    

    #* Tab 2
    def tab2_select_input_file(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFile)
        fd.setDirectory('C:\\')
        if fd.exec():
            self.tab2_input_file_path = fd.selectedFiles()[0]
            self.tab2_input_file.setText(self.tab2_input_file_path)

    def tab2_select_output_folder(self):
        self.tab2_output_folder_path = QFileDialog().getExistingDirectory(self, "Select Directory", "C:\\")
        self.tab2_output_file.setText(self.tab2_output_folder_path)

    def tab2_select_private_key_file(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFile)
        fd.setDirectory('C:\\')
        if fd.exec():
            self.tab2_private_key_file_path = fd.selectedFiles()[0]
            self.tab2_private_key_file.setText(self.tab2_private_key_file_path)

    def tab2_select_encrypted_symmetric_key_file(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFile)
        fd.setDirectory('C:\\')
        if fd.exec():
            self.tab2_encrypted_symmetri_key_file_path = fd.selectedFiles()[0]
            self.tab2_encrypted_symmetri_key_file.setText(self.tab2_encrypted_symmetri_key_file_path)

    def tab2_confirm(self):
        isInput = False
        isOutput = False
        isPrivateKey = False
        isSymKey = False
        isChoice = False
        if self.tab2_input_file_path != None:
            isInput = True
        if self.tab2_output_folder_path != None:
            isOutput = True
        if self.tab2_private_key_file_path != None:
            isPrivateKey = True
        if self.tab2_encrypted_symmetri_key_file_path != None:
            isSymKey = True
        if self.tab2_encrypt_Btn.isChecked() or self.tab2_decrypt_Btn.isChecked():
            isChoice = True

        if isInput and isOutput and isPrivateKey and isSymKey and isChoice:
            if self.tab2_encrypt_Btn.isChecked():   # perform encryption
                filename = os.path.basename(self.tab2_input_file_path)
                filename = self.check_file_duplicate_with_bin(f'encrypted_{filename}', self.tab2_output_folder_path)
                output_filename = f'{filename}.bin'
                output_file = os.path.join(self.tab2_output_folder_path, output_filename)
                try:
                    # encryption
                    Prog_Encrypt.encrypt_file_with_RSA_given_AES_key(self.tab2_input_file_path, output_file, self.tab2_private_key_file_path, self.tab2_encrypted_symmetri_key_file_path)
                except: # hv error for encryption
                    QMessageBox.warning(None, 
                             'File Management System', 
                             '<html><head/><body><p><span style=\" font-size:15pt;\">Fail to Encrypt</span></p></body></html>'
                             '<html><head/><body><p><span style=\" font-size:11pt;\">Wrong private key file or encrypted symmetric key file</span></p></body></html>',
                             QMessageBox.StandardButton.Ok, 
                             QMessageBox.StandardButton.Ok)
                    
                else:   # No error for encryption
                    while not os.path.isfile(output_file):
                        continue
                    self.show_success('Finish File Encryption', output_filename)
            else:   # perform decryption
                filename = os.path.splitext(os.path.basename(self.tab2_input_file_path))[0]     # assume filename has 2 file extention (e.g. test.pdf.bin)
                filename, ext = os.path.splitext(filename)
                if ext == '': # input file only have 1 extention -> give .bin as ext for the decrypted file
                    filename = f'{filename}.bin'
                else:
                    filename = filename + ext
                filename = self.check_file_duplicate(f'decrypted_{filename}', self.tab2_output_folder_path)
                output_file = os.path.join(self.tab2_output_folder_path, filename)
                try:
                    Prog_Encrypt.decrypt_file_with_RSA_AES_without_pwd(self.tab2_input_file_path, output_file, self.tab2_private_key_file_path, self.tab2_encrypted_symmetri_key_file_path)
                except:
                    QMessageBox.warning(None, 
                             'File Management System', 
                             '<html><head/><body><p><span style=\" font-size:15pt;\">Fail to Decrypt</span></p></body></html>'
                             '<html><head/><body><p><span style=\" font-size:11pt;\">Wrong private key file or encrypted symmetric key file</span></p></body></html>',
                             QMessageBox.StandardButton.Ok, 
                             QMessageBox.StandardButton.Ok)
                else:
                    while not os.path.isfile(output_file):
                        continue
                    self.show_success('Finish File Decryption', filename)

        else:   # not fill in all the option
            self.show_not_complete_warning()


    #* Tab 3
    def tab3_select_input_file(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFile)
        fd.setDirectory('C:\\')
        if fd.exec():
            self.tab3_input_file_path = fd.selectedFiles()[0]
            self.tab3_input_file.setText(self.tab3_input_file_path)

    def tab3_select_output_folder(self):
        self.tab3_output_folder_path = QFileDialog().getExistingDirectory(self, "Select Directory", "C:\\")
        self.tab3_output_file.setText(self.tab3_output_folder_path)

    def tab3_select_private_key_file(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFile)
        fd.setDirectory('C:\\')
        if fd.exec():
            self.tab3_private_key_file_path = fd.selectedFiles()[0]
            self.tab3_private_key_file.setText(self.tab3_private_key_file_path)
    
    def tab3_select_public_key_file(self):
        fd = QFileDialog()
        fd.setFileMode(QFileDialog.FileMode.ExistingFile)
        fd.setDirectory('C:\\')
        if fd.exec():
            self.tab3_public_key_file_path = fd.selectedFiles()[0]
            self.tab3_public_key_file.setText(self.tab3_public_key_file_path)

    def tab3_confirm(self):
        isInput = False
        isOutput = False
        isPrivateKey = False
        isPublicKey = False
        if self.tab3_input_file_path != None:
            isInput = True
        if self.tab3_output_folder_path != None:
            isOutput = True
        if self.tab3_private_key_file_path != None:
            isPrivateKey = True
        if self.tab3_public_key_file_path != None:
            isPublicKey = True
        if self.tab3_encrypt_Btn.isChecked() or self.tab3_decrypt_Btn.isChecked():
            pass
        else:
            self.show_not_complete_warning()

        if self.tab3_encrypt_Btn.isChecked():   # perform encryption
            if isInput and isOutput and isPublicKey:    # filled all required field
                file_size = os.path.getsize(self.tab3_input_file_path)
                if file_size > 245: # check whether the input file is larger than 245 bytes
                    QMessageBox.critical(None, 
                                         'File Management System', 
                                        '<html><head/><body><p><span style=\" font-size:15pt;\">Input file size is larger than 245 byte</span></p></body></html>'
                                        '<html><head/><body><p><span style=\" font-size:11pt;\">The public key encryption(RSA) is not available.</span></p></body></html>',
                                        QMessageBox.StandardButton.Ok, 
                                        QMessageBox.StandardButton.Ok)
                    return

                filename = os.path.basename(self.tab3_input_file_path)
                filename = self.check_file_duplicate_with_bin(f'encrypted_{filename}', self.tab3_output_folder_path)
                output_filename = f'{filename}.bin'
                output_file = os.path.join(self.tab3_output_folder_path, output_filename)
                try:
                    # encryption
                    Prog_Encrypt.encrypt_file_with_RSA(self.tab3_input_file_path, output_file, self.tab3_public_key_file_path)
                except: # hv error for encryption
                    QMessageBox.warning(None, 
                                'File Management System', 
                                '<html><head/><body><p><span style=\" font-size:15pt;\">Fail to Encrypt</span></p></body></html>'
                                '<html><head/><body><p><span style=\" font-size:11pt;\">Wrong public key file</span></p></body></html>',
                                QMessageBox.StandardButton.Ok, 
                                QMessageBox.StandardButton.Ok)
                    
                else:   # No error for encryption
                    while not os.path.isfile(output_file):
                        continue
                    self.show_success('Finish File Encryption', output_filename)
            else:   # some required option is missing
                QMessageBox.warning(None, 
                             'File Management System', 
                             '<html><head/><body><p><span style=\" font-size:15pt;\">Not Complete</span></p></body></html>'
                             '<html><head/><body><p><span style=\" font-size:11pt;\">Input File, Output Folder or Public Key File is missing.</span></p></body></html>',
                             QMessageBox.StandardButton.Ok, 
                             QMessageBox.StandardButton.Ok)

        elif self.tab3_decrypt_Btn.isChecked():   # perform decryption
            if isInput and isOutput and isPrivateKey:    # filled all required field
                filename = os.path.splitext(os.path.basename(self.tab3_input_file_path))[0]     # assume filename has 2 file extention (e.g. test.pdf.bin)
                filename, ext = os.path.splitext(filename)
                if ext == '': # input file only have 1 extention -> give .bin as ext for the decrypted file
                    filename = f'{filename}.bin'
                else:
                    filename = filename + ext
                filename = self.check_file_duplicate(f'decrypted_{filename}', self.tab3_output_folder_path)
                output_file = os.path.join(self.tab3_output_folder_path, filename)
                try:
                    Prog_Encrypt.decrypt_file_with_RSA(self.tab3_input_file_path, output_file, self.tab3_private_key_file_path)
                except:
                    QMessageBox.warning(None, 
                                'File Management System', 
                                '<html><head/><body><p><span style=\" font-size:15pt;\">Fail to Decrypt</span></p></body></html>'
                                '<html><head/><body><p><span style=\" font-size:11pt;\">Wrong Private Key File or Input File</span></p></body></html>',
                                QMessageBox.StandardButton.Ok, 
                                QMessageBox.StandardButton.Ok)
                else:
                    while not os.path.isfile(output_file):
                        continue
                    self.show_success('Finish File Decryption', filename)

            else:   # some required option is missing
                QMessageBox.warning(None, 
                             'File Management System', 
                             '<html><head/><body><p><span style=\" font-size:15pt;\">Not Complete</span></p></body></html>'
                             '<html><head/><body><p><span style=\" font-size:11pt;\">Input File, Output Folder or Private Key File is missing.</span></p></body></html>',
                             QMessageBox.StandardButton.Ok, 
                             QMessageBox.StandardButton.Ok)



    #* Other
    # check if have duplicated file in the destination path
    def check_file_duplicate_with_bin(self, filename, folder_path):
        isDuplicate = True
        base_name, ext = os.path.splitext(filename)
        count = 0
        while isDuplicate:
            isDuplicate = False
            for check_filename in os.listdir(folder_path):
                if check_filename == f'{filename}.bin':
                    isDuplicate = True
                    count += 1
                    filename = f"{base_name} ({count}){ext}"
                    break
        return filename
    
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

    def show_success(self, title, filename):
        QMessageBox.information(None, 
                                    'File Management System', 
                                    f'<html><head/><body><p><span style=\" font-size:15pt;\">{title}</span></p></body></html>'
                                    f'<html><head/><body><p><span style=\" font-size:11pt;\">{filename}</span></p></body></html>',
                                    QMessageBox.StandardButton.Ok, 
                                    QMessageBox.StandardButton.Ok)

    def show_not_complete_warning(self):
        QMessageBox.warning(None, 
                             'File Management System', 
                             '<html><head/><body><p><span style=\" font-size:15pt;\">Not Complete</span></p></body></html>'
                             '<html><head/><body><p><span style=\" font-size:11pt;\">Please complete all options.</span></p></body></html>',
                             QMessageBox.StandardButton.Ok, 
                             QMessageBox.StandardButton.Ok)

