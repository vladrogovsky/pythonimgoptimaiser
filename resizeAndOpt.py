import sys
from PIL import Image 
import os
from fnmatch import fnmatch
def update_progress(progress):
    print '\r[{0}] {1}%'.format('#'*(progress/10), progress)

def resizeImg(img):
	im=Image.open(img)
	origSize = im.size
	sizeH = [768,768]
	sizeW = [600,600]
	if (origSize[1]>768 and origSize[1]>origSize[0] ):
         im.thumbnail(sizeH, Image.ANTIALIAS)
         im.save(img, "JPEG")
	elif (origSize[0]>600 and origSize[0]>origSize[1] ):
         im.thumbnail(sizeW, Image.ANTIALIAS)
         im.save(img, "JPEG")
	
def startGuetzli(img,output="",path=""):
	if (path == ""):
		path = os.path.dirname(os.path.realpath(__file__))
		print(path)
		print("\n\r")
	if (output == ""):
		output = img
	cmd = path+'\guetzli.exe --verbose "'+img+'" "'+output+'"'
	print(cmd)
	print("\n\n")
	os.system(cmd)


root = raw_input('Enter a root directory: ')
dirList = []
pattern = ["*.jpg","*.jpeg"]

print("Currently using such pattern for files:\n\r")
print(pattern)
print("\n\r")
start = raw_input('To start enter [Y/y] or [N/n] to exit: ')

if (start == "Y" or start == "y" or start == ""):
	for path, subdirs, files in os.walk(root):
	    for name in files:
	    	for patterVal in pattern:
		        if fnmatch(name, patterVal):
		            dirList.append(os.path.join(path, name))
elif (start == "N" or start == "n"):
	exit()


percentPerItm = 100/len(dirList)
currentProg = 0

print("Resizing images...")
update_progress(currentProg)

for oneFile in dirList:
	resizeImg(oneFile)
	currentProg+=percentPerItm
	update_progress(currentProg)


currentProg = 0
print("Done.\n\r")
print("Start images optimization..")
update_progress(currentProg)

for oneFile in dirList:
	startGuetzli(oneFile)
	currentProg+=percentPerItm
	update_progress(currentProg)