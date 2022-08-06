"""Bulk File Rename

   Not the most intuitive I admit, but it does work. Will add improved functionality as I progress in my studies. 
"""


import os
import sys

folder = os.path.dirname(input(r"Enter the path of a folder: "))

if os.path.isdir(folder):
    print('Folder Found')
    
else:
    print("Folder Path Not Found")
    exit()

new_file_name = input("Enter new filename: ")
new_file_ext = input("Enter the extension: ")      
for count, filename in enumerate(os.listdir(folder), 1):
    dst = f"{new_file_name}{str(count)}"
    src = f"{folder}/{filename}"
    dst = f"{folder}/{dst}"
    
    os.rename(src, dst + new_file_ext)