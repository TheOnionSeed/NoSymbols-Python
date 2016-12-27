#This program reads in a file
#and remove all symbols within a file and 
#output the new data to a new file
#Created by: Tri Do
import re

file = open("origFile.txt", "r")#change origDictionary.txt with an old file
outputFile = open("outputFile.txt","w")#the new file that we will write to

#read the original file by getting each line
contents=file.read()#contents is a list with all the lines
file.close()

outputContents = re.sub('[-!$%^&*()_+|~=`{}\[\]:";\'<>?,.\/]','', contents)


#output the new string to a new file
outputFile.write(outputContents);
outputFile.close();
