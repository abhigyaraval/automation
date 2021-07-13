# Functions required for the sort_files project

from os import listdir
from os.path import isfile, join
import os
import shutil
from file_types_dict import file_type_dict

# Main function for sorting
def sort_files_in_a_folder (mypath):
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    file_type_variation_list = []
    filetype_folder_dict = {}
    for file in files:
        try:
            filetype = file.split('.')[1]
            print(filetype)
        except:
            filetype = ""
        if filetype not in file_type_variation_list:
            file_type_variation_list.append(filetype)

            for key in file_type_dict:
                if filetype == key:
                    folder_name_part = file_type_dict[key]
                    break
                else:
                    folder_name_part = 'Misc'
            new_folder_name = mypath+'/'+folder_name_part+' '+'files'
            filetype_folder_dict[str(filetype)] = str(new_folder_name)
            if os.path.isdir(new_folder_name) == True:      # Folder exists
                continue
            else:
                os.mkdir(new_folder_name)
    for file in files:
        src_path = mypath+'/'+file
        try:
            filetype = file.split('.')[1]
            print(filetype)
        except:
            filetype = ""
        if filetype in filetype_folder_dict.keys():
            dest_path = filetype_folder_dict[str(filetype)]
            shutil.move(src_path, dest_path)
            print(src_path + '>>>>>' + dest_path)


