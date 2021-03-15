class duit:
    #enkapsulasi adalah penetuan hak akses ke variabel dan method
    #di enkapsulasi ada 3 hak akses yaitu public,private,protected

    #list untuk menghafal enkapsulasi python
    #
    # 1.)Public= tidak memakai underscore/garis bawah pada atribut
    #contoh:baju,celana,dasi
    # 2.)Private= memakai 2 under score sebelum nama atribut
    #contoh:__gula,__garam,__merica
    # 3.)Protected= memakai 1 under score sebelum nama atribut
    #contoh:_ayah,_ibu,_anak

    def __init__ (self):
        self.__dollar=14000
    def tukar(self):
        print("Nilai tukar uang Dollar ke rupiah adalah {}".format(self.__dollar))
    def rupiah(self,rp):
        self.dollar=rp
    def __tabungan(self,tabung):
        self.tabung=tabung
        print("Tidak dapat meliihat tabungan saya")
        print("Tabungan saya sejumlah=",tabung)
    def nama(self):#pembuatan 
        self._nama="Diando"
        print("Nama nasabah=",self._nama)




money=duit()#instansiasi
money.tukar()#public
#money.__tabungan(1000000)#private pada method
money.nama()#protected pada nama


