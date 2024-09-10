import json
import os
import hashlib

import Config as Prog_config

USERS_FILE = "users.json"

# auth_hash = sha356_hash(pwd||username)
class User:
    def __init__(self, username: str, pwd: str):
        self.username = username
        self.pwd = pwd
        self.auth_hash = self.toHash()
        self.privateKey = None
    
    def toDic(self):
        return {
            'username': self.username, 
            'auth_hash': self.auth_hash
        }
    
    def toHash(self):
        string = self.pwd + self.username
        return sha256_hash(string)

    def empty(self):
        self.username = ''
        self.pwd = ''
        self.auth_hash = ''
        self.privateKey = ''

def sha256_hash(string):
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()

    # Convert the string to bytes and update the hash object
    sha256.update(string.encode('utf-8'))

    # Get the hexadecimal representation of the hash value
    hash_value = sha256.hexdigest()

    return hash_value

# build a empty users.json file if it doesn't exist
def build_users_json_file(config_path):
    json_path = os.path.join(config_path, USERS_FILE)
    if not os.path.isfile(json_path):
        with open (json_path, 'w') as file:
            json.dump([], file)

def signIn(config_path, user: User):
    json_path = os.path.join(config_path, USERS_FILE)
    with open(json_path, 'r') as file:
        users_data = json.load(file)

    if len(users_data) == 0:    # users.json has no record
        return [False, "The username does not exist."]
    else:   # users.json has record
        for u in users_data:
            if user.username == u['username']:  # has such username
                if user.auth_hash == u['auth_hash']:    # right pwd
                    return [True]
                else:   # wrong pwd
                    return [False, "Wrong password. Please enter again."]
        # no such username
        return [False, "The username does not exist."]


def signUp(config_path, user: User):
    json_path = os.path.join(config_path, USERS_FILE)
    with open(json_path, 'r') as file:
        users_data = json.load(file)    # extract data from users.json
    
    same = False
    if len(users_data) == 0:    # empty json file
        pass
    else:                       # json file contains records
        for u in users_data:
            if user.username == u['username']:  # json file contain same username
                same = True
                return [False, 'The username already exists.']
    # No same username -> record the user's info [Successful Sign Up]
    if same == False:
        users_data.append(user.toDic())     # add data to the arr
        with open(json_path, 'w') as file:  # write data to users.json
            json.dump(users_data, file, ensure_ascii=False, indent=4)

        # add user
        return [True]

# build the user folder and keyEncypt & passEncypt folder for later saving encypted files
def build_user_folder(folder_path, username):
    users_folder = os.path.join(folder_path, 'users')
    user_folder = Prog_config.create_folder(users_folder, username)
    Prog_config.create_folder(user_folder, 'config')
    keyEncypt_folder = Prog_config.create_folder(user_folder, 'keyEncrypt')
    Prog_config.create_folder(user_folder, 'passEncrypt')
    Prog_config.create_folder(keyEncypt_folder, 'files')
    Prog_config.create_folder(keyEncypt_folder, 'keys')


# def build_dic_json_file(path, file_name):
#     json_path = os.path.join(path, file_name)
#     if not os.path.isfile(json_path):
#         with open (json_path, 'w') as file:
#             json.dump({}, file)

