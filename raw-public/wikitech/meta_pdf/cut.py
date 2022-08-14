#! /bin/python3
import os
import shutil

files = os.listdir('./')
files.remove('.DS_Store')
files.remove('cut.py')
files = sorted(files)
# import pdb; pdb.set_trace()
for i in range(1, 38):
    dirs = str(i)
    if not (os.path.exists(dirs)):
        os.mkdir(dirs)
    for j in range(0,10):
        index = (i - 1) * 10 + j
        shutil.move(files[index], dirs)