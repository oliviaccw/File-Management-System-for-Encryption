from PyQt6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
import os, datetime

import Login as Prog_login

    
# check duplicate with encrypted files
def check_duplicate(file_path, folder_path):
    check_filename = os.path.basename(file_path)
    for file_name in os.listdir(folder_path):
        file_name = file_name = file_name.rsplit(".bin", 1)[0]
        if file_name == check_filename:
            return None
    return check_filename

def is_integer(number):
    number = str(number)
    arr = number.split('.')
    if (len(arr) == 1):
        return True
    else:
        return False

def format_file_size(size_in_bytes):
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    unit_index = 0

    while size_in_bytes >= 1024 and unit_index < len(units) - 1:
        size_in_bytes /= 1024
        unit_index += 1

    if is_integer(size_in_bytes):
        return f"{int(size_in_bytes)} {units[unit_index]}"
    else:
        return f"{size_in_bytes:.2f} {units[unit_index]}"

def get_file_items_list(folder_path):
    folder_items = []
    if len(os.listdir(folder_path)) == 0:
        return []
    else:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            file_size = os.path.getsize(file_path)
            file_size = format_file_size(file_size)
            file_modified_date = os.path.getmtime(file_path)
            file_modified_date = datetime.datetime.fromtimestamp(file_modified_date).strftime("%d/%m/%Y %H:%M")
            empty_item = QStandardItem('')
            empty_item.setFlags(empty_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            file_name = file_name.rsplit(".bin", 1)[0]
            file_name_item = QStandardItem(file_name)
            file_name_item.setFlags(file_name_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            file_size_item = QStandardItem(file_size)
            file_size_item.setFlags(file_size_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            file_date_item = QStandardItem(file_modified_date)
            file_date_item.setFlags(file_date_item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            file_items = [file_name_item, file_size_item, file_date_item]
            folder_items.append(file_items)

    return folder_items



