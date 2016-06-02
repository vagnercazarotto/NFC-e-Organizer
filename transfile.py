### vagner@tkcode.com
### A simple way to organize XML files from multi stores  
### organized in date year + month + store number
import datetime
from ftplib import FTP 
import os
import io
import time
import sys 
import socket 

try:
	argv = sys.argv[1:]
except ValueError:
		pass

if "--version" in argv or "-v" in argv:
		print "VERSAO 1.0.3"
		sys.exit()
	

###  INI files
# you can change this for you default folder 
fileTarget     = open("C:\\rjm\\fileList.ini",'r')
startINI       = fileTarget.read().split()
ftpServer      = startINI[0].split("=")[1]
userName       = startINI[1].split("=")[1]
password       = startINI[2].split("=")[1]
storeNumber    = startINI[3].split("=")[1]
backupFolder   = startINI[4].split("=")[1]
custodiaFolder = startINI[5].split("=")[1]
fileTarget.close()
###

## change directory name
monthName ={
	0:"drop",
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"}



## start connection 
ftp =  FTP(ftpServer)
ftp.login(user=userName,passwd=password) 
## keep Alive
ftp.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

## receive a list of directiories 
docList = ftp.nlst()

### Block verify - mkdir and got to folder 
### create a folder name from actual date
folderName = datetime.datetime.now().strftime("%Y"+"_"+"%B") + "_loja_" + str(storeNumber)
for x in docList:
	if folderName == x:
		cont = 1
		ftp.cwd(folderName)
		break
	else:
	 	cont = 0
if cont == 0:
	ftp.mkd(folderName)
	ftp.cwd(folderName)
####

## receive a list of directiories 
fileList = ftp.nlst()


### control send files
itemList = os.listdir(backupFolder)
dateNow = datetime.datetime.now().strftime("%Y"+"_"+"%B")
for x in itemList:
	fileCreation = os.path.getctime(backupFolder + x)
	initialDate = datetime.datetime.fromtimestamp(fileCreation).strftime("%Y"+"_"+"%B")
	if dateNow == initialDate:
		if x not in fileList:
			print "Enviando Arquivo!!"
			print str(backupFolder + x)
			ftp.storbinary('STOR ' + str(x) , open(str(backupFolder + x),'rb'))


## do the same for custodia folder 			
itemList = os.listdir(custodiaFolder)
dateNow = datetime.datetime.now().strftime("%Y"+"_"+"%B")
for x in itemList:
	fileCreation = os.path.getctime(custodiaFolder + x)
	initialDate = datetime.datetime.fromtimestamp(fileCreation).strftime("%Y"+"_"+"%B")
	if dateNow == initialDate:
		if x not in fileList:
			print "Enviando Arquivo!!"
			print str(custodiaFolder + x)
			ftp.storbinary('STOR ' + str(x) , open(str(custodiaFolder + x),'rb'))


#### Verify last month

## now go to root folter 
ftp.cwd("/")

## receive a list of directiories 
docList = ftp.nlst()

month =  monthName[datetime.datetime.now().month-1]
year = datetime.datetime.now().year
lastMonth = str(year) + "_" + str(month) 
folderName = str(lastMonth) + "_loja_" + str(storeNumber)

for x in docList:
	if folderName == x:
		cont = 1
		ftp.cwd(folderName)
		break
	else:
	 	cont = 0
if cont == 0:
	ftp.mkd(folderName)
	ftp.cwd(folderName)
####

## receive a list of directiories 
fileList = ftp.nlst()


### control send files
itemList = os.listdir(backupFolder)
for x in itemList:
	fileCreation = os.path.getctime(backupFolder + x)
	initialDate = datetime.datetime.fromtimestamp(fileCreation).strftime("%Y"+"_"+"%B")
	if lastMonth == initialDate:
		if x not in fileList:
			print "Enviando Arquivo!!"
			print str(backupFolder + x)
			ftp.storbinary('STOR ' + str(x) , open(str(backupFolder + x),'rb'))

## do the same for custodia folder 

itemList = os.listdir(custodiaFolder)
for x in itemList:
	fileCreation = os.path.getctime(custodiaFolder + x)
	initialDate = datetime.datetime.fromtimestamp(fileCreation).strftime("%Y"+"_"+"%B")
	if lastMonth == initialDate:
		if x not in fileList:
			print "Enviando Arquivo!!"
			print str(custodiaFolder + x)
			ftp.storbinary('STOR ' + str(x) , open(str(custodiaFolder + x),'rb'))


## close connection
ftp.quit()

