#!/bin/bash

python script.py $1
mkdir $1
cd $1
git init
touch README.md 
git add .
git commit -m "first commit"
git remote add origin https://github.com/santiagoconde0/$1.git
git push -u origin master