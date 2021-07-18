# setiap objek yang direpresentasikan dalam program berbasis OOP
# merupakan bentuk nyata dari sebuah konsep yang disebut class
# class merupakan kerangka utama (blueprint) dari objek

'''CLASS ATTRIBUTE'''
# adalah properti/atribut yang bernilai sama untuk seluruh objek dari sebuah class
# Definisikan class Karyawan
class Karyawan:
    nama_perusahaan = 'ABC'
# Inisiasi object yang dinyatakan dalam variabel aksara dan senja
aksara = Karyawan()
senja = Karyawan()
# Cetak nama perusahaan melalui penggunaan keyword __class__
# pada class attribute nama_perusahaan
print(aksara.__class__.nama_perusahaan)
# Ubah nama_perusahaan menjadi 'DEF'
aksara.__class__.nama_perusahaan = 'DEF' # otomatis akan diubah pada seluruh objek
# Cetak nama_perusahaan objek aksara dan senja
print(aksara.__class__.nama_perusahaan)
print(senja.__class__.nama_perusahaan)


'''INSTANCE ATTRIBUTE'''
# adalah properti/atribut yang nilainya berbeda-beda untuk setiap objek dari sebuah class
# fungsi __init__() disebut sebagai konstruktor yang dpt menginisialisasi atribut milik objek
# Definisikan class Karyawan
class Karyawan:
    nama_perusahaan = 'ABC'
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
# Buat object bernama aksara dan senja
aksara = Karyawan('Aksara', 25, 8500000)
senja = Karyawan('Senja', 28, 12500000)
# Cetak objek bernama aksara
print(aksara.nama + ', Usia: ' + str(aksara.usia) + ', Pendapatan ' + str(aksara.pendapatan))
# Cetak objek bernama senja
print(senja.nama + ', Usia: ' + str(senja.usia) + ', Pendapatan ' + str(senja.pendapatan))



'''BEHAVIOUR PADA CLASS'''
# Definisikan class Karyawan berikut dengan attribut dan fungsinya
class Karyawan:
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur
    def tambahan_proyek(self, insentif_proyek):
    	self.pendapatan_tambahan += insentif_proyek
    def total_pendapatan(self):
    	return self.pendapatan + self.pendapatan_tambahan
# Buat object dari karwayan bernama Aksara dan Senja
aksara = Karyawan('Aksara', 25, 8500000)
senja = Karyawan('Senja', 28, 12500000)
# Aksara melaksanakan lembur
aksara.lembur()
# Senja memiliki proyek tambahan
senja.tambahan_proyek(2500000)
# Cetak pendapatan total Aksara dan Senja
print('Pendapatan Total Aksara: ' + str(aksara.total_pendapatan()))
print('Pendapatan Total Senja: ' +str(senja.total_pendapatan()))