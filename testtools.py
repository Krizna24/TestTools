#python
#program

import time
import os
op='''
    ______________________________
   | Hey, Kont*ol                 |
   | Mau Coba Program ku?         |
   |                              |
   |   •Yoh gelem                 |
   |   •Orak!!!                   |
   |                              |
   |                              |
   |______________  ______________|
             _____||_____
             Kriz   Tools

'''
os.system("clear")
print (op)
print ("Y/N")
slc=input("   >>> ")
if slc==("Y") or slc==("y"):
   isi='''
    ______________________________
   | Dipilih, shuk :v             |
   |                              |
   |   1.install LinuxOS          |
   |   2.install Tool-X Kali      |
   |                              |
   |                              |
   |                              |
   |______________  ______________|
             _____||_____
             Kriz   Tools
   '''
   time.sleep(1)
   os.system("clear")
   time.sleep(1)
   print (isi)
   plh=input("   Masukin Nomer nya bujank : ")
   if plh=="2":
      time.sleep(1)
      print ("loading")
      time.sleep(2)
      os.system("clear")
      os.system("pkg update;pkg upgrade;pkg install git;git clone https://github.com/Rajkumrdusad/Tool-X;cd Tool-X;chmod +x *;sh install.aex")
      time.sleep(1)
      os.system("clear")
      print ("wes diinstallke yo, su")
      print ('carane nganggo gari ngetik "Tool-X"')
      time.sleep(1)
   if plh=="1":
      time.sleep(1)
      print ("loading")
      time.sleep(2)
      os.system("clear")
      os.system("pkg update;pkg upgrade;pkg install git;pkg install python2;git clone https://github.com/jaksa976/TermuxOS")
      time.sleep(1)
      os.system("clear")
      print ("wes diinstallke yo, su")
      print ('carane nganggo gari mlebu folder TermuxOS "cd TermuxOS" njur ngetik "python2 LinuxOS.py"')

if slc=="N" or slc=="n":
   time.sleep(1)
   print ("A Yo uwes :v")
