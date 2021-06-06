#!python3 - Automate the creation of files in all courses folder
import shutil, os, zipfile, send2trash, re
# open the required folder
# create a file called notes.md in the folder

def find_subfolder(regex_pattern):
    # this loop walks through the current working directory
    subfolder_path_list = [] # create a list of empty subfolders.
    for folder_name, subfolders, filenames in os.walk(os.getcwd()):
        for subfolder in subfolders:
            #this loop uses regrex to search for subfolders.
            if regex_pattern.search(subfolder):
                path = os.path.join(folder_name,subfolder)
                subfolder_path_list.append(path) # add items to list
    return subfolder_path_list

def insert_file(file_name, regex_pattern, content=''):
    for folder in find_subfolder(regex_pattern):
        with open(os.path.join(folder,file_name), 'w') as new_file:
            new_file.write(content)

# create the regex for folder names.
all_files_pattern = re.compile(r'[A-Z]+\d+$')

#print(find_subfolder(all_files_pattern))

insert_file('notes.md', all_files_pattern)
