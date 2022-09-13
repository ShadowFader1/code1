import os
import shutil

from_dir="D:/System_Data/Downloads/nm.pdf"
to_dir="D:/System_Data/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name,ext = os.path.splitext(i)

print(name)
print(ext)