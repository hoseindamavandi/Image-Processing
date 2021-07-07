import cv2
import os
import shutil

folders = os.listdir("MNIST_persian")
print(folders)
src = "MNIST_persian"
target = "MNIST_persian_organized"
os.mkdir(target)
for folder in folders:
    newfolder = src +"/" + folder
    files = os.listdir(newfolder)
    for file in files:
        srcfile=newfolder+"/"+file
        namefile = file.split(".")
        creatfolder = target + "/" + namefile[0]
        creatfile = creatfolder +"/" +namefile[0] + "-" +folder+".jpg"
        if os.path.isdir(creatfolder) == False:
            os.mkdir(creatfolder)
        shutil.copy2(srcfile, creatfile)
