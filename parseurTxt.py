import os
import sys


pdfDir = sys.argv[1]
outputDirName = "TEXT"
resultsDirName = "RESULTS"


def getName(fileName):
	name = os.path.basename(fileName)
	name = os.path.splitext(name)[0]

	
	f = open(resultsDirName+"/"+name+".txt", "w")
	f.write(name+"\n")
	f.close()
	


if os.path.exists(outputDirName):
	for files in os.listdir(outputDirName):
		fileDir = outputDirName+"/"+files
		os.remove(fileDir)
	
	os.rmdir(outputDirName)	
	
	
os.mkdir(outputDirName)


if os.path.exists(resultsDirName):
	for files in os.listdir(resultsDirName):
		fileDir = resultsDirName+"/"+files
		os.remove(fileDir)
	
	os.rmdir(resultsDirName)	
	
	
os.mkdir(resultsDirName)


for fileName in os.listdir(pdfDir):
	name = os.path.basename("/"+pdfDir+"/"+fileName)
	name = os.path.splitext(name)[0]
	
	pdfFile = pdfDir+"/"+name+".pdf"
	targetFile = outputDirName+"/"+name+".txt"

	command = "pdf2txt -A -t text "+pdfFile+" -o "+targetFile
	os.system(command)


for fileName in os.listdir(outputDirName):
	getName(fileName)

