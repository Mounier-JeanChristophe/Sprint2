# Sprint2
Dépôt- Séance 2 TP IL

## Fonctionnement 
le fichier prog.cpp ouvre deux fichiers .txt à la fois, le premier fichier en lecture et le deuxiéme en écriture ou j'écris par la suite les sections (nom de fichier d'origine, titre, abstract). on a décidé de convertir les fichiers pdf en fichier html afin d'avoir la fin exacte des sections. dans un premier temps je lis  mon fichier d'entrée (html) jusqu'a que ma condition se réalise (je trouve ma balise <title>) aprés je renvoie un nouveau objet string qui contient que mon titre grace a les deux methode find qui renvoie la position de la chaine qui est en parametre et la methode substr qui renvoie la sous chaine. ...

(a continuer ) 

## commandes 

**convertion pdf**
> pdftotext -raw -layout  Boudin-Torres-2006.pdf -bbox