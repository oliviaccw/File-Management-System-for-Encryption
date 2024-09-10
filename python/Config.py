import os

# Name of the folder of storing all the files
FOLDER_NAME = "FileManagmentSys_ProgramFiles"

# txt file to save the path of storing files
CONFIG_FILE = "config_fileManagement.txt"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# check if user already have the CONFIG_FILE in the computer
def check_config_exists():
    return os.path.isfile(CONFIG_FILE)

def load_path_from_config():
    with open(CONFIG_FILE, "r") as file:
        return file.readline()

def create_folder(path, folder_name):
    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def set_folder_path(folder_path):
    # Create the folder
    path = create_folder(folder_path, FOLDER_NAME)

    # Record the path in the config file
    with open(CONFIG_FILE, "w") as config:
        config.write(path)
