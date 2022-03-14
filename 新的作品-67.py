import os,shutil

files = os.listdir()
print(files)

# file_info = os.stat("bcm.jpg")
# print(file_info)

# suffix = os.path.splitext("bcm. jpg")
# print(suffix)

myDir = "BCM"
if not os.path.exists(myDir):
    os.mkdir(myDir)

images_ext = [".png",".jpg",".bmp",".jpeg",".gif"]
for file in files:
    ext = os.path.splitext(file)[-1]
    if ext in images_ext:
        shutil.copy(file,myDir)
        print(file) 
