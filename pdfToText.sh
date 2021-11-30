#!/bin/bash

if [ ! -d "TEXT" ] 
then
    $(mkdir TEXT)
fi


for fich in $(find $1 -name "*.pdf" | cut -d"/" -f2)
do
    txt=$(echo $fich | cut -d"." -f1)".txt"
    $(pdf2txt -A -t "text" $1/$fich -o TEXT/$txt)
done

