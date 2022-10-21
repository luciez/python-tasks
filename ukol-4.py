class Recept:
    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev=nazev
        self.narocnost=narocnost
        self.url_adresa=url_adresa
        self.vyzkouseno=False
    
    def __str__(self):
        if self.vyzkouseno==False:
            return f"VYZKOUŠEJ! Recept {self.nazev} (náročnost:{self.narocnost}). Najdeš ho na adrese {self.url_adresa}."
        else:
            return f"UVAŘ SI ZNOVA! Recept {self.nazev} (náročnost:{self.narocnost}) najdeš na adrese {self.url_adresa}."
    
    def zmen_narocnost(self, nova_hodnota):
        self.narocnost=nova_hodnota

    def zkusit(self):
        self.vyzkouseno=True

class Kucharka:
    def __init__(self,nazev,autor):
        self.nazev=nazev
        self.autor=autor
        self.recepty=[]
    
    def __str__(self):
        return f"NOVINKA PRO MILOVNÍKY RÝŽE: {self.nazev} od autora s pseudonymem {self.autor} obsahuje sbírku rizot různých obtížností. "
    
    def pocet_receptu(self):
        return len(self.recepty)
    
    def pridej_recept(self,recept):
        self.recepty.append(recept)

recept1=Recept("Šťavnaté rizoto","Střední","https://www.vareni.cz/recepty/stavnate-rizoto/")
recept2=Recept("Lososové rizoto s parmazánem","Vysoká","https://www.vareni.cz/recepty/lososove-rizoto-s-parmazanem-1615306474678/")
recept3=Recept("Zeleninové rizoto s kuřecím masem","Střední","https://www.vareni.cz/recepty/zeleninove-rizoto-s-kurecim-masem/")

recept1.zmen_narocnost("Nízká")
recept2.zkusit()

Rizota=Kucharka("Rýžová rizota z rýže", "Rýžový Král")
Rizota.pridej_recept (recept3)
