#This program reads in a file
#and remove all symbols within a file and 
#output the new data to a new file
#Created by: Tri Do
import re

file = open("origDictionary.txt", "r")#change origDictionary.txt with an old file
outputFile = open("dictionary.txt","w")#the new file that we will write to

#read the original file by getting each line
contents=file.readlines()#contents is a list with all the lines
file.close()

outputContents = ""


#go through each line and check each string
#if it contains a non-letter or non-numbers
#then remove all the symbols from that line
for line in contents:
	if not(re.match("^[A-Za-z0-9]*$", line)):
		line  = re.sub("[!@#$%^&*()_+-={}[]|\:;<,>.?/~`']", '', line)
	outputContents += line
	

#output the new string to a new file
outputFile.write(outputContents);
outputFile.close();