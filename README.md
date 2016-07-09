# NFC-e-Organizer

 The Electronic Nota Fiscal (NFe), also known as National Nota Fiscal, is an XML file required by the Brazilian government that replaces the paper Nota Fiscal. So this is a simple way to organize the XML files from sales point and then send to counter office.


# Installation

$ git clone https://github.com/vagnercazarotto/NFC-e-Organizer.git \n
$ cd NFC-e-Organizer \n
$ python build.py  \n
$ transfile \n

# Usage 

Edite the **fileList.ini** file, and then incorporate a call to **transfile.exe** in your routine.

ftpserver= your.ftpserver \n
user= your.username \n 
password= your.password \n
loja= your.storeName \n 
backupFolder=C:\\NFCE\\BACKUP\\      << you can change for your default folder \n
custodiaFolder=C:\\NFCE\\CUSTODIA\\  << you can change for your default folder \n


# Contributing 

Changes and improvements are mora than welcome! Feel free to fork and open a pull request. Please make your 
changes in a specific branch and request to pull into 'master'.

# Licence

NFC-e-Organizer is licensed under the MIT license.
