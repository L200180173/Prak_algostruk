class Pesan(object):
    """
        Sebuah class bernama pesan.
        Untuk memahami konsep class dan object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai',len(self.teks),'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru

#1.a
    def apakahTerkandung(self, j):
        if j in self.teks:
            return True
        else:
            return False

#1.b
    def hitungKonsonan(self):
        konsonan = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        jumlah = 0
        a = self.teks
        for i in a:
            if i in konsonan:
                jumlah += 1
        return jumlah

#1.c
    def hitungVokal(self):
        vokal = "aiueoAIUEO"
        jumlah = 0
        b = self.teks
        for i in b:
            if i in vokal:
                jumlah += 1
        return jumlah
