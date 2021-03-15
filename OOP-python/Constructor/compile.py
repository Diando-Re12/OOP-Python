#sebelum kesini,pastikan sudah paham materi yang awal

class compile:
    #kali ini kita akan membahas tentang  konstruktor
    #konstruktor adalah membuat sebuah objek pada sebuah kelas
    #misalkan kalian punya sawah,emang disawah itu ada apa aja?


    #ketika sudah bisa mengetahui hal itu,langsung saja buka komentar yg sudah saya sematkan pada  dibawah ini

    def __init__(self,jam,menit,detik): #ini adalah konstruktor dimana atribut yang saya pakai adalah jam,menit,detik
        
        self.jam=jam 
        self.menit=menit
        self.detik=detik
        

#main        
compile1=compile(1,12,30)
compile2=compile(0,59,38)
compile3=compile(1,10,18)


print("Waktu untuk compile ke 1 adalah= {} jam {} menit {} jam".format(compile1.jam,compile1.menit,compile1.detik))
print("Waktu untuk compile ke 2 adalah= {} jam {} menit {} menit".format(compile2.jam,compile2.menit,compile2.detik))
print("Waktu untuk compile ke 3 adalah= {} jam {} menit {} detik".format(compile3.jam,compile3.menit,compile3.detik))
