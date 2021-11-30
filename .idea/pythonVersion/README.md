
    ***** explication pour le Sprint 2 *****

les fonction que on a utilisé dans ce sprint :

# parser_file_to_txt : 
cette fonction permet de extraire les informations demandé dans un fichier ".txt" 
elle creer un nouveau fichier .txt et le place dans le chemin passé en parametre (output_path)

# create_directory :
cette fonction permet de creer un dossier :

- dossier qui centient les ficher sont convertié (pdf -> txt)
- dossier qui centiernt les fichier les informations (nom du fichier, titre, abstract) avec l'extention .txt

# find_paragraph :
cette fonction permet de chercher une paragraphe selon d'un titre que passe dans l'argument de la fonction 

# pdf_to_txt :
cette fonction permet de convertir un fichier de extention PDF a une autre extention TXT
elle deplace le fichier de resultat dans le chemin passé en parametre

# find_ext : 
cette fonction permet de chercher tout les ficher dans un dossier on le passe dans le parametre de la fonction 
et qui finnissent par une extention passé aussi en parametre de la fonction 








### ------------ Comment on excute le code --------------  :

il faut en premier installer la commande pdftotext

il faut taper la commande suivant dans le terminal des commandes (LINUX) 

python3 main.py (chemin de dossier qui centient les fichier .pdf) 