from burung import *#saya menggunakan import karena berada di file yg berbeda
#jadi saya dapat mengakses objek burung


#class takterbang saya umpamakan sebagai class anak

class takterbang(burung):
    #namun diclass anak,disini ada tambahan atribut berupa terbang
    def __init__(self,bulu,bertelur,terbang):
        self.bulu=bulu
        self.bertelur=bertelur
        self.terbang=terbang
    
    def infotakterbang(self):
        print("\n====================\nBurung yang tidak bisa terbang")
        print("Memiliki bulu=",self.bulu)
        print("Bisa berterlur=",self.bertelur)
        print("Bisa terbang=",self.terbang)

databurung=takterbang("iya","iya","tidak")
databurung.infotakterbang()