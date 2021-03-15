import os
'''
File handling adalah penanganan file yang mengatur proses CRUD

sintaks file handling
r=read/membaca file
w=write/menulis file dan mengedit file yang ada
a=append/menambahkan
b=binary mode(contoh foto)
t=teks
delete file=menggunakan import os
(os.remove(file):digunakan untuk delete file)
(os.rmdir(folder):digunakan untuk delete folder)

'''

#membuka file dengan file handling
file=open("eksekusi.txt","r")
print(file.read())

#membuka file dipath lain
file1=open("G:\OOP-python\ikan.txt","r")
print(file1.read())

#menampilkan beberapa karakter pada file
file2=open("eksekusi.txt","r")
print(file2.read(4))

#menutup file
file4=open("G:\OOP-python\ikan.txt","r")
print(file1.read())
file4.close()

#append/menambahkan tulisan dibelakang file

file5=open("ubah.txt","a")
file5.write("Tambahkan kalimat ini")
file5.close()
file5=open("ubah.txt","r")
print(file5.read())

#write/mengedit file
file6=open("ubah.txt","w")
file6.write("Ubah kalimat ini")
file6.close()
file6=open("ubah.txt","r")
print(file6.read())

#hapus file dan folder

file7=os.remove("hapus.txt")
file8=os.rmdir("hapus-folder")