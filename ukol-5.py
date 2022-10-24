#https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/ukol-05.md
class Nemoc:
    # poradi argumentu v radku nize si klidne preskladejte
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Jmeno: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti

class Koronavirus(Nemoc):
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        super().__init__(jmeno, inkubacni_doba, pocet_obeti, sireni)
        self.varianty=[]
    
    def zmen_pocet_obeti(self, pocet_obeti):
        return super().zmen_pocet_obeti
    
    def pridej_variantu(self, varianta):
        self.varianty.append(varianta)

    