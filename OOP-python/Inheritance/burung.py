#Inheritance merupakan konsep penurunan sifat/pewarisan
#dari milik induk ke milik si anak


#class burung saya umpamakan sebagai class induk
class burung:
    #diclass induk kita hanya melihat hanya ada dua atribut disini
    #yaitu bulu dan bertelur,jadi bangsa burung itu biasanya berbulu
    #ataupun reproduksi dengan cara bertelur
    def __init__(self,bulu,bertelur):
        self.bulu=bulu
        self.bertelur=bertelur

    def info(self):
        print("Burung")
        print("Memiliki bulu=",self.bulu)
        print("Bisa berterlur=",self.bertelur)

databurung=burung("iya","iya")
databurung.info()