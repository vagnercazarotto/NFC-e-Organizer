# NFC-e-Organizer

 The Electronic Nota Fiscal (NFe), also known as National Nota Fiscal, is an XML file required by the Brazilian government that replaces the paper Nota Fiscal. So this is a simple way to organize the XML files from sales point and then send to counter office.


# Installation

<p>$ git clone https://github.com/vagnercazarotto/NFC-e-Organizer.git </p>
<p>$ cd NFC-e-Organizer </p>
<p>$ python build.py  </p>
<p>$ transfile </p>

# Usage 

Edite the **fileList.ini** file, and then incorporate a call to **transfile.exe** in your routine.

<p>ftpserver= your.ftpserver </p>
<p>user= your.username </p>
<p>password= your.password </p>
<p>loja= your.storeName </p>
<p>backupFolder=C:\\NFCE\\BACKUP\\      << you can change for your default folder </p>
<p>custodiaFolder=C:\\NFCE\\CUSTODIA\\  << you can change for your default folder </p>


# Contributing 

Changes and improvements are mora than welcome! Feel free to fork and open a pull request. Please make your 
changes in a specific branch and request to pull into 'master'.

# Licence

NFC-e-Organizer is licensed under the MIT license.
