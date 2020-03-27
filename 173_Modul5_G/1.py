from kegiatan5 import *

class MhsTIF(object):
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', nim ' + str(self.nim)\
            + '. Tinggal di ' + self.kota\
            + '. Uang saku Rp ' + str(self.uangSalu)\
            + '. tiap bulannya.'
        return s

m0 = MhsTIF("Riska", 132, "Magetan", 120000)
m1 = MhsTIF("Fira", 190, "Madiun", 670000)
m2 = MhsTIF("Siwi", 100, "Batang", 890000)
m3 = MhsTIF("Naura", 292, "Madiun", 35000)
m4 = MhsTIF("Aviza", 112, "Surabaya", 290000)
m5 = MhsTIF("Nina", 199, "Purwodadi", 200000)
m6 = MhsTIF("Sekar", 301, "Medan", 248000)
m7 = MhsTIF("Ulin", 899, "padang", 265000)
m8 = MhsTIF("Tata", 387, "Pontianak", 295000)
m9 = MhsTIF("Ichi", 201, "Banten", 279000)
m10 = MhsTIF("Nimas", 227, "Klaten", 205000)

Daftar = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

def urutNim(list):
    NIM = []
    for i in list:
        NIM.append(i.nim)
    insertionSort(NIM)
    return NIM

print(urutNim(Daftar))
