import requests
import os
import random
import sys
import time
from time import sleep 
os.system('clear')
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.4)
#ubah angka 0.1 sesuai keinginan kamu
#angka terkecil adalah yang paling cepat
#angka terbesar adalah yang paling lambat
print ('\033[1;32m')
print('loading..')
sleep(0.1)
mengetik('> > > > > > > > > > > > > 100%')
sleep(1)  
os.system('clear')
def main():
   password = input ('masukkan kata sandi broo.. :')
   if password == 'sableng87':
       print ('kata sandi diterima broo..')
       sleep(2)
       os.system('clear')
   else:
        print ('kata sandi salah broo..')
main()
os.system('clear')
def cekip():
 print(f'[!] Mendapatkan IP..')
 re = requests.get('https://api.myip.com').json()
 ip = re['ip']
 print(f'[!] IP kamu : {ip}')
def iOsif():
 print(f'[!] Menginstall tools osif..')
 os.system('pkg update upgrade')
 os.system('pkg install git python2')
 os.system('git clone https://github.com/ciku370/OSIF')
 os.system('cd OSIF')
 os.system('pip2 install -r requirements.txt')
 os.system('python2 osif.py')
def spamsms():
 print(f'[!] Menginstall tools spamsms..')
 os.system('pkg update && pkg upgrade')
 os.system('pkg install bash')
 os.system('pkg install git')
 os.system('git clone https://github.com/kumpulanremaja/spam-sms.git')
 os.system('cd spam-sms')
 os.system('bash spam.sh') 

mengetik('''-=[ [̲̅W̲̅][̲̅E̲̅][̲̅L̲̅][̲̅C̲̅][̲̅O̲̅][̲̅M̲̅][̲̅E̲̅]  [̲̅I̲̅][̲̅N̲̅]  [̲̅M̲̅][̲̅Y̲̅]-[̲̅T̲̅][̲̅O̲̅][̲̅O̲̅][̲̅L̲̅][̲̅S̲̅] ]=-
============================
Tools Installer SABLENG87
============================
     -=[Menu]=-
[1] Cek IP
[2] Install OSIF
[3] Install spamsms
[4] keluar
''')
menu = input('[?] Silahkan pilih menu : ')

if menu == '1':
 cekip()
elif menu == '2':
 iOsif()
elif menu == '3':
 spamsms()
elif menu == '4':
 print('[?] Keluar..')
 sys.exit()
else:
 print('[?] Perintah tidak diketahui..')
 sys.exit()
