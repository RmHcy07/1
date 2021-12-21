import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'='*40)
print(a+'\t\033[31;1mTombol Tambahan Termux ')
print(a+'\t\033[33;1mUP,Down,right,Left, CTRL ')
print('\t\033[34;1mBy : R4M4DH4N1')
print('\t\033[35;1mFacebook : RAMA GANZ')
print('\t\033[36;1mLO SEMUA SEMPAK')
print(a+'='*40)
print('\nLoanjing...')
sleep(1)
print(b+'\n\033[33;1m[●] Pencopotan File Lama.....')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[●]Success !')
sleep(1)
print(b+'\n[●] Menambahkan File Baru.....')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[●] Memproses  !')
sleep(1)
print(b+'\n[●] Pemasangan EXtra-Keys ')
sleep(2)
os.system('termux-reload-settings')
print(a+'[●] Proses Selesai !! '+c+'\n\nJan Di Recode Ya !\n\n')
