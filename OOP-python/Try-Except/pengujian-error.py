#try except adalah proses pengujian error pada sebuah program hal ini sangat bermanfaat untuk mengetahui segala kesalahan dan memberikan peringatan

#kondisi ketika benar
'''
x=30

try:
    print(x)
except:
    print("ERROR")

'''

#kondisi ketika salah
'''
try:
    print(x)
except:
    print("ERROR")
'''

#kondisi ketika salah lainnya
'''
try:
    print(c)
except NameError:#ini akan dieksekusi
    print("Tidak ada variabel c disini")
except:
    print("Keluar")
'''

#finally/proses akhir
'''
try:#ini yg akan berjalan,tapi bisa juga dibuat salah untuk mengetahui exceptnya
    file=open("G:\OOP-python\ikan.txt","r")
    print(file.read())
except:
    print("Tidak ada file ini")
finally:#proses ini akan dilakukan try&except diekseskusi
    file.close()
'''
#raise Exception(membuat Except)

'''
nama=12
if not type(nama)is str:#jika nama tidak termasuk string,maka akan ada type Error
    raise TypeError("Coba tuliskan itu dengan String")
'''