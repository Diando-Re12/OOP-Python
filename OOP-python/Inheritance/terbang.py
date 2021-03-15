from burung import *#saya menggunakan import karena berada di file yg berbeda
#jadi saya dapat mengakses objek burung

#class terbang saya umpamakan sebagai class anak
class terbang(burung):
    #namun diclass anak,disini ada tambahan atribut berupa terbang
    def __init__(self,bulu,bertelur,terbang):
        self.bulu=bulu
        self.bertelur=bertelur
        self.terbang=terbang
    
    def infoterbang(self):
        print("\n====================\nBurung yang bisa terbang")
        print("Memiliki bulu=",self.bulu)
        print("Bisa berterlur=",self.bertelur)
        print("Bisa terbang=",self.terbang)

databurung=terbang("iya","iya","iya")
databurung.infoterbang()

