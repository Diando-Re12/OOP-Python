class komandan:
    
    def __init__(self,nama,pekerjaan):
        self.nama=nama
        self.__pekerjaan=pekerjaan
        

    @property

    def info(self):
        return "Nama Anggota= {}".format(self.nama)

    #getter
    @property
    
    def pekerjaan(self):
        pass

    #setter
    @pekerjaan.setter

    def pekerjaan(self,input):
        self.__pekerjaan=input
    
    #deleter(menghapus getter setter)
    @pekerjaan.deleter

    def pekerjaan(self):
        print("Telah dipecat")
        self.pekerjaan=None

#info
print("Rumor mengatakan bahwa ada boss baru yang akan datang")
print("untuk menggantikan Arief Dan dia bernama Hasan")
Arief=komandan("Arief","Boss")
print(Arief.info)
print(Arief.__dict__)
Arief.nama="Hasan"
print(Arief.info)
print(Arief.__dict__)


#print getter and setter
print("Mengenai pekerjaan Hasan,selain menjadi Boss.Dia juga menjadi")
print("Dia menjadi komando sebuah organisasi militer")
print("\n\n\n===================\n\ngetter setter untuk __pekerjaan")
print(Arief.pekerjaan)
print(Arief.__dict__)
Arief.pekerjaan="Komandan"
print(Arief.pekerjaan)
print(Arief.__dict__)

#cek menghapus atribut

print("\n\nDikarenakan Hasan tidak becus kerja,jadi ia dipecat")
print("\n\n\n===================\n\nHapus Pekerjaan Arief")
del Arief.pekerjaan
print(Arief.__dict__)

