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
	

def getTittle(fileName):

	textFile = open(outputDirName+"/"+fileName, "r")
	resultFile = open(resultsDirName+"/"+fileName, "a")
	
	compteurLigne = 0
	for line in textFile:
		
		if ("pages" in line.lower() or "letter" in line.lower() or "by" in line.lower()) or any(char.isdigit() for char in line) or len(line) <= 2:
			pass
		else:	
			
			if line != "\n":
				compteurLigne = compteurLigne + 1
				
				if compteurLigne == 1:
					line = line.replace("\n","")
					resultFile.write(line+" ")

				if compteurLigne == 2:
					resultFile.write(line)
					break


	textFile.close()
	resultFile.close()
	
def getAbstract(fileName):

	findIntro = False
	findAbstract = False

	abstractLineBreak = 0


	textFile = open(outputDirName+"/"+fileName, "r")
	resultFile = open(resultsDirName+"/"+fileName, "a")

	for line in textFile:
		if "abstract" in line.lower():
			findAbstract = True
			if "abstract\n" == line.lower():
				continue

		if "article" in line.lower(): 
			findAbstract = True

		if findAbstract and findIntro == False:
			if abstractLineBreak > 2 or "introduction" in line.lower() or (len(line) <= 3 and line != "\n") or line[0] == '1':
				findIntro = True
				break

			if line == "\n":	
				abstractLineBreak = abstractLineBreak + 1

			if "." in line:
				line = line.split(".",1)
				line[0] = line[0]+"."
				resultFile.write(line[0]+"\n")
				
				if line[1] != "\n":
					newLine = line[1].split(" ",1)
					newLine[1] = newLine[1].replace("\n"," ")
					resultFile.write(newLine[1])		
			else:
				if abstractLineBreak == 1:
					line = line.replace("\n","")
				else:
					line = line.replace("\n"," ")
				resultFile.write(line)	
				


	textFile.close()
	resultFile.close()




#START OF EXECUTION


''' 
#Création du dossier TEXT qui contiendra les fichier .txt à la suite de la commande : pdf2txt (maintenant réalisé par le script shell)
#Utile dans le cas où le script python doit le faire seul

if os.path.exists(outputDirName):
	for files in os.listdir(outputDirName):
		fileDir = outputDirName+"/"+files
		os.remove(fileDir)
	
	os.rmdir(outputDirName)	
	
	
os.mkdir(outputDirName)
'''

#Création du dossier RESULTS qui contiendra les fichier .txt après récupération des différentes sections
if os.path.exists(resultsDirName):
	for files in os.listdir(resultsDirName):
		fileDir = resultsDirName+"/"+files
		os.remove(fileDir)
	
	os.rmdir(resultsDirName)	
	
	
os.mkdir(resultsDirName)

''' #Lancement de la commande pdf2txt pour chaque fichier pdf contenu dans le dossier passé en argument (maintenant réalisé par le script shell)

for fileName in os.listdir(pdfDir):
	name = os.path.basename("/"+pdfDir+"/"+fileName)
	name = os.path.splitext(name)[0]
	
	pdfFile = pdfDir+"/"+name+".pdf"
	targetFile = outputDirName+"/"+name+".txt"

	command = "pdf2txt -A -t text "+pdfFile+" -o "+targetFile
	os.system(command)

'''

command = "./pdfToText.sh "+pdfDir
os.system(command)

for fileName in os.listdir(outputDirName):
	getName(fileName)
	getTittle(fileName)
	getAbstract(fileName)
