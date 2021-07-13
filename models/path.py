import os, shutil
from os import listdir
from os.path import isfile, join
mypath = r'C:\Users\Toan\OneDrive\Desktop\YouTube_DataSet_Annotated\action_youtube_naudio'
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    # f.extend(filenames)
    for file in filenames:
        if '.avi' in file:
            f.append(os.path.join(dirpath, file))
            shutil.move(os.path.join(dirpath, file), r'C:\Users\Toan\OneDrive\Desktop\YouTube_DataSet_Annotated\videos')
print(f)
