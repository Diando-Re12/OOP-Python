# Apa itu Object-Oriented Programming (OOP)?
# Pemrograman berorientasi objek, atau OOP singkatnya, adalah paradigma
# pemrograman yang menyediakan sarana untuk menyusun program sehingga sifat dan perilaku digabungkan menjadi objek individual. Misalnya, objek bisa mewakili seseorang dengan nama properti, umur, alamat, dll, dengan perilaku seperti berjalan, berbicara, bernafas, dan berlari. Atau email dengan properti seperti daftar penerima, subjek, badan, dll., Dan perilaku seperti menambahkan lampiran dan pengiriman.

class rumah:#ini adalah cara pembuatan class
    #Kelas merupakan template untuk atribut2 yang ingin dimasukkan


    #untuk membuat atributnya,kita gunakan magic word __init__ untuk inisialisasi

    #contoh instance
    def __init__(self,panjang,lebar):#<------------------|
        #                                        |       |
        #ini merupakan atribut yg dipakai        |       |
        self.panjang=panjang#--------------------        |
        self.lebar=lebar#<-------------------------------

#melakukan instansiasi kepada objek rumah

#cara melakukan instansiasi yaitu dengan format seperti ini:

#nama_objek=nama_class(argumen,argumen)

gubuk=rumah(3,5)
perumahan=rumah(9,15)
apartemen=rumah(4,6)

#mengakses atribut

print("Ukuran untuk gubuk adalah= {} x {} hektar".format(gubuk.panjang,gubuk.lebar))
print("Ukuran untuk perumahan adalah= {} x {} hektar".format(perumahan.panjang,perumahan.lebar))
print("Ukuran untuk apartemen adalah= {} x {} hektar".format(apartemen.panjang,apartemen.lebar))

# Fungsi format() menerima dua parameter yaitu:

# value – nilai atau objek yang butuh diformat
# format_spec (opsional) – spesifikasi tentang bagaimana nilai atau objek tersebut akan diformat

# disini saya gunakan format untuk objek yg telah saya buat agar dimasukkan sesuai