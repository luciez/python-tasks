from datetime import datetime, timedelta, date, time, tzinfo

premium_od=datetime(2021, 7, 1)
premium_do=datetime(2021, 8, 10)
premium_cena=250
lowcost_od=datetime(2021, 8, 11)
lowcost_do=datetime(2021, 8, 31)
lowcost_cena=180

pozadovane_datum=input("Kdy plánuješ kino navštívit: ")
pocet_vstupenek=int(input("Kolik vstupenek kupuješ: "))

def vytvor_datetime(datum):
    return datetime.strptime(datum, "%d. %m. %Y")

def vrat_cenu_vstupenky(datum_navstevy):
    if datum_navstevy >= premium_od and datum_navstevy <= premium_do:
        return premium_cena
    elif datum_navstevy >= lowcost_od and datum_navstevy <= lowcost_do:
        return lowcost_cena
    else:
        return 0

def vypocet_ceny(cena_za_kus, pocet_vstupenek):
    if cena_za_kus==0:
        print("Tento den nehrajeme. Vyber si datum mezi 1. 7. a 31. 8. 2021.")
    else:
        print(f"Zaplatíš celkem {cena_za_kus*pocet_vstupenek} Kč.")

datum_navstevy=vytvor_datetime(pozadovane_datum)
cena_za_kus=vrat_cenu_vstupenky(datum_navstevy)
vypocet_ceny(cena_za_kus, pocet_vstupenek)
#print(celkem)

