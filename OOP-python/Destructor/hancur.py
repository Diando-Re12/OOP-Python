#Destructor merupakan kebalikan dari konstruktor,dimana destructor berfungsi
#untuk menghancurkan sebuah objek

class hancur:

    def __init__(self):
        print("masih ada")
    #penambahan untuk destructor ada disini,dimana __del__ berfungsi untuk
    #menghapus objek
    def __del__(self):
        print("telah terhapus")

coba=hancur()
coba1=coba
coba2=coba
#kondisi saat belum terken destructor
print(id(coba),id(coba1),id(coba2))

del coba
del coba1
del coba2

#setelah terkena destructor
print(id(coba),id(coba1),id(coba2))
