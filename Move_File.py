import os
import shutil

from_dir = "C:/Users/alexa/Desktop/Python/Class 102/c102/image_files"
to_dir = "Document_Files"

list_of_files =  os.listdir(from_dir)
#print(list_of_files)

for i in list_of_files:
    files, extention=os.path.splitext(i)
    if extention == "":
        continue
    if extention in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + "/" + i
        path2 = to_dir + "/" + "image_files"
        path3 = to_dir + "/" + "image_files" + '/'+i
        if os.path.exists(path2):
            print("Moving...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving...")
            shutil.move(path1, path3)