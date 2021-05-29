import os

path = "C:/Users/HP/OneDrive/Documents/THE BIG RED GROUP"

for root, sub_folders, files in os.walk(path):

    print(str(root) + "Root")
    print(str(sub_folders) + "Sub Folders")
    print(str(files) + "Files")
