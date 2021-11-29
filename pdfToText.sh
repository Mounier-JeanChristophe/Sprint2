#!/bin/bash

if [ ! -d "Text" ] 
then
    $(mkdir Textfile)
fi

for fich in $(find -name "*.pdf")
do
    $(pdftotext $fich)
done

for fich in $(find -name "*.txt")
do
    $(mv $fich Textfile/)
done