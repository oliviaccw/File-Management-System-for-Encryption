from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QFileDialog
import sys, os

import Config as Prog_Config
import Login as Prog_Login
from Login import User
import View.Config, View.Login, View.MainWindow

     

if __name__ == '__main__':
    app = QApplication(sys.argv)

    folder_path = None
    show_config_ui = False
    if Prog_Config.check_config_exists():   # have the config txt file
        folder_path = Prog_Config.load_path_from_config().strip()
        if folder_path == "" or not os.path.exists(folder_path):
            show_config_ui = True
    else:
        show_config_ui = True
    
    # If doesn't have the config file, show the config window
    # If the config file is empty or the recorded path not exist, show the config window
    if show_config_ui:
        config_ui = View.Config.Ui_Form()
        config_ui.show()
        config_exit = app.exec()
    
    # User doesn't choose any folder and close the config window
    if show_config_ui and not Prog_Config.check_config_exists():
        sys.exit(config_exit)

    # get path from the file after user set the path by config window
    if show_config_ui: 
        folder_path = Prog_Config.load_path_from_config()

    # Build a 'config' directory under the 'FileManagementSys' directory for saving the app's config files
    config_path = Prog_Config.create_folder(folder_path, 'config')
    users_path = Prog_Config.create_folder(folder_path, 'users')

    # build users.json file if not yet have
    Prog_Login.build_users_json_file(config_path)

    # For login
    login_ui = View.Login.Ui_Form() # new login window obj
    login_ui.folder_path = folder_path  # pass the folder path for building user folder after sucessful sign up
    login_ui.config_path = config_path  # pass the config_path
    login_ui.show()
    login_exit = app.exec()

    # User close the login window without sucessful login
    if login_ui.user == None:
        sys.exit(login_exit)

    # Get the User obj after successful login
    user = login_ui.user


    # Open the main window; pass users path data & user obj
    mainWindow_ui = View.MainWindow.Ui_MainWindow(users_path, user)
    mainWindow_ui.show()    # show the main window
    
    sys.exit(app.exec())

