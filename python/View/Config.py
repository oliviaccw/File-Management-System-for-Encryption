from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QFileDialog

import Config as Prog_Config


class Ui_Form(QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.config_path = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(511, 403)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(50, 70, 50, 50)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font-size: 14px;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(7, 5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "File Management System"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt;\">Get Start!</span></p></body></html>"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Please enter the path where you want to store the files:</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Choose a folder"))
        self.confirm_Btn.setText(_translate("Form", "Confirm"))

    def select_folder(self):
        self.config_path = QFileDialog().getExistingDirectory(self, "Select Directory", "C:\\")
        self.path_input.setText(self.config_path)

    def confirm(self):
        Prog_Config.set_folder_path(self.config_path)
        