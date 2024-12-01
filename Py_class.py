
class Imparatorluk:
    yil = 1400
    eyalet = 64
    hazine = 600000
    gelir = 80000
    gider = -60000
    ordu = 50000

    def baslangic(self):
        print(f"""Yıl: {self.yil}
        Eyalet sayısı: {self.eyalet}
        Hazine: {self.hazine} altin  Gelir: {self.gelir} altin  Gider: {self.gider} altin
        Ordu: {self.ordu} asker""")
        
    def yatirim(self):
        self.hazine-=50000
        self.gelir+=10000
        print(f"""Yıl: {self.yil}
        Eyalet sayısı: {self.eyalet}
        Hazine: {self.hazine} altin  Gelir: {self.gelir} altin  Gider: {self.gider} altin
        Ordu: {self.ordu} asker""")

    def fetih(self):
        self.ordu-=5000
        self.eyalet+=1
        self.gelir+=5000
        print(f"""Yıl: {self.yil}
        Eyalet sayısı: {self.eyalet}
        Hazine: {self.hazine} altin  Gelir: {self.gelir} altin  Gider: {self.gider} altin
        Ordu: {self.ordu} asker""")

    def tur_atla(self):
        self.yil+=1
        self.hazine+=self.gelir+self.gider
        print(f"""Yıl: {self.yil}
        Eyalet sayısı: {self.eyalet}
        Hazine: {self.hazine} altin  Gelir: {self.gelir} altin  Gider: {self.gider} altin
        Ordu: {self.ordu} asker""")

    def ordu_al(self):
        self.hazine-=5000
        self.ordu+=5000
        print(f"""Yıl: {self.yil}
        Eyalet sayısı: {self.eyalet}
        Hazine: {self.hazine} altin  Gelir: {self.gelir} altin  Gider: {self.gider} altin
        Ordu: {self.ordu} asker""")


imp = Imparatorluk()

imp.baslangic()
imp.yatirim()
imp.tur_atla()
imp.ordu_al()
imp.fetih()