import os
from os import listdir
from os.path import isfile, join
mypath = os.getcwd()
onlyfiles = []
for f in listdir(mypath):
	if f.endswith(".asc"):
		onlyfiles.append(f)
# Open a new file to write the data to
newfile = open("Combined_Data.asc",'w')
# Open each file to be copied one-at-a-time and read them into newfile.
for f in onlyfiles:
	currentfile = open(f, 'r')
	readfile = currentfile.readlines()
	currentfile.close()
	linecounter = 1
	for line in readfile:
		if linecounter <= 256: 
			line = 'flower '+ f[0:(len(f)-4)]+str(linecounter)+' '+line
			newfile.write(line)
			linecounter += 1
newfile.close()
