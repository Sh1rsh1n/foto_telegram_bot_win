import os
import random


def walking_all_files(directory):
    files_list = []
    for folders, subfolders, files in os.walk(directory):
        for file in files:
            if file[-4::] in ('.jpg', '.jpeg', '.heic'):
                files_list.append(os.path.abspath(file))
    return files_list


def get_random_file(file_list: list):
    return random.choice(file_list)

ls = walking_all_files('C:/Java')
print(len(ls), '\n', ls)