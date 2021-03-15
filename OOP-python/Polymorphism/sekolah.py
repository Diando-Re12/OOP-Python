#kelas induk
class sekolah: 
    def kenal(self): 
        print("Sekolah memiliki banyak tingkat.") 
	
    def jenjang(self): 
	    print("Tingkatan di sekolah disebut jenjang.") 
#kelas anak	
class SMP(sekolah):
    #Overriding dari kelas induk
    def jenjang(self): 
	    print("Aku masih SMP.") 
#kelas anak
class SMA(sekolah): 
    #Overriding dari kelas induk
    def jenjang(self): 
	    print("Aku masih SMA.") 
	
Sekolah = sekolah() 
smp = SMP() 
sma = SMA() 


print(Sekolah.kenal())
print(smp.jenjang())
print(sma.jenjang())

