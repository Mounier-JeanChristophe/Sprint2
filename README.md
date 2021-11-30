PARSEUR PDF to TEXT

Réalisé en Python / Made in Python

---------- Dépendances / Dependencies ----------

Nécessite la librairie popper-utils
Nécessite d'appeler le script avec pour unique argument le dossier qui contiendra les fichiers PDF.
Nécessite d'appeler le script "pdfToText.sh"


Requires popper-utils library
Requires calling the script with the single argument the folder that will contain the PDF files.
Requires calling the script "pdfToText.sh"

---------- Comment ça fonctionne ? / How it works ? ----------

Le script python crée un dossier "RESULTS" pour stocker les fichiers résultats.
Ensuite, le script exécute le script shell qui va créer des fichiers textes (dans un nouveau dossier TEXT) ayant le contenu des fichiers PDF.
Le programme en python isole alors, pour chaque fichier, trois sections. 
Le dossier TEXT contiendra les fichiers PDF convertis en fichier .txt
Le dossier RESULTS contiendra des fichiers textes avec seulement les trois sections recherchées.

Chaque partie que l'on souhaite isoler va être rechercher puis écrite à la suite du fichier.txt résultat.
Il récupère le nom du fichier (1ère ligne).
Il récupère les titres des fichiers PDF. (A partir de la 2ème ligne).
Il récupère les résumés de chaque fichier PDF (De la 3ème/4ème ligne jusqu'à la fin du fichier)


The python script creates a "RESULTS" folder to store the results files.
Then, the script executes the shell script which will create text files (in a new TEXT folder) having the contents of the PDF files.
The python program then isolates, for each file, three sections.
TEXT folder will contain PDF files converted to .txt file
The RESULTS folder will contain text files with only the three searched sections.

Each part that we want to isolate will be searched for then written after the result file.txt.
It retrieves the name of the file (1st line).
It recovers the titles of PDF files. (From the 2nd line).
It recovers the summaries of each PDF file (From the 3rd / 4th line to the end of the file)

---------- Comment l'exécuter ? / How to run it ? ----------

Syntaxe : VERSION_PYTHON parseur.py DOSSIER_SOURCE
Syntax : PYTHON_VERSION parseur.py SOURCE_DIRECTORY

Exemple / Example : python3 parseur.py PDF
