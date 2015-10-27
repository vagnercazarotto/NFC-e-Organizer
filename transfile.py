### vagner@tkcode.com
### A simple way to organize XML files from multi stores  
### organized in date year + month + store number
import datetime
from ftplib import FTP 
import os
import io
import time


###  INI files
# you can change this for you default folder 
fileTarget  = open("C:\\rjm\\fileList.ini",'r')
startINI    = fileTarget.read().split()
ftpServer   = startINI[0].split("=")[1]
userName    = startINI[1].split("=")[1]
password    = startINI[2].split("=")[1]
storeNumber = startINI[3].split("=")[1]
xmlFolder 	= startINI[4].split("=")[1]
print xmlFolder
fileTarget.close()
###

## start connection 
ftp =  FTP(ftpServer)
ftp.login(user=userName,passwd=password) 

## receive a list of directiories 
docList = ftp.nlst()



### Block verify - mkdir and got to folder 
### create a folder name from actual date
folderName = datetime.datetime.now().strftime("%Y"+"_"+"%m") + "_loja_" + str(storeNumber)
for x in docList:
	if folderName == x:
		cont = 1
		break
	else:
	 	cont = 0
if cont == 0:
	ftp.mkd(folderName)
for x in docList:
	if folderName == x:
		ftp.cwd(folderName)
		break
####

## receive a list of directiories 
fileList = ftp.nlst()


### control send files
z = 0 
itemList = os.listdir(xmlFolder)
dateNow = datetime.datetime.now().strftime("%Y"+"_"+"%m")
for x in itemList:
	fileCreation = os.path.getctime(xmlFolder + x)
	initialDate = datetime.datetime.fromtimestamp(fileCreation).strftime("%Y"+"_"+"%m")
	if x not in fileList:
		print "Enviando Arquivo!!"
		print str(xmlFolder + x)
		ftp.storbinary('STOR ' + str(x) , open(str(xmlFolder + x),'rb'))


## close connection
ftp.quit()
