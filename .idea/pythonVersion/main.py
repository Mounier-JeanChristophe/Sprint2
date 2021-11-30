from os import path
import os
from glob import glob
import sys



#recherche les fichiers dans le dossier passé en parametre (chemin_dossier)
#qui finissent par l'extension passé en parametre.

def find_ext(chemin_dossier, ext):
    return glob(path.join(chemin_dossier, "*.{}".format(ext)))



def pdf_to_txt(inpute_path, output_path) :
    cmd = "pdftotext " + inpute_path + " " + output_path
    os.system(cmd)


def find_paragraph(file_path, titre):
    paragraph = ""
    with open(file_path, "r") as file :
        for line in file :
            if(line.lower().find(titre) != -1):
                if(len(line) <= len(titre)+1):
                        line = file.readline()
                        while line == "\n":
                            line = file.readline()
                while line:
                    if(line == "\n") :
                        break
                    paragraph = paragraph + line.strip().lower().strip(titre)
                    line = file.readline()
                if(paragraph != "\n"):
                    return paragraph
    return "Not Found\n"

#cree un dossier passe en parametre "dossier" dans le chemin passé en parametre "chemin"
def create_directory(dossier, chemin):
    directory_name = dossier
    path = chemin + "/" + directory_name
    if(os.path.isdir(path)):
        os.system("rm -r " + path)                  #supprimer le dossier s'il exit    
    os.system("mkdir " + path)                      #re creer le dossier
    return path    



def parser_file_to_txt(filepath, output_path) :

    file_name = os.path.basename(filepath).replace(".txt", ".pdf")
    title = ""
    abstract = ""
    #   -- nom de fichier --

    f = open(output_path, "a")
    f.write("le nom de ce fichier est : " + file_name + "\n")
    f.close()

    f = open(filepath, "r")
    for i in range(2) :
        title = title + f.readline().strip('\n').strip() + " "
    f.close()
    #   -- le titre de fichier --

    f = open(output_path, "a")
    f.write("\n\n le titre de ce fichier est  : " + title.rstrip() + "\n")
    f.close()
    #   -- abstract --

    abstract = find_paragraph(filepath, "abstract")
    f = open(output_path, "a")
    f.write("\n\n abstract : " + abstract)
    f.close()

def main():
    args = sys.argv
    filepath = args[1]   # on prends l'argument apres la commande python3 (chemin de dossier) si le code est dans le meme dossier des fichier il suffit just de mettre le nom de dossier                
    dossier_txt = create_directory("File_txt", filepath)
    dossier_output = create_directory("output", filepath)
    files = find_ext(filepath,"pdf")

    for file in files :
            File_txt_path = dossier_txt + "/" + os.path.basename(file).replace(".pdf", ".txt")
            output_path = dossier_output + "/" + os.path.basename(file).replace(".pdf", ".txt") 
            pdf_to_txt(file, File_txt_path)
            parser_file_to_txt(File_txt_path, output_path)

if __name__ == "__main__":
    main()