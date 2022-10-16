#https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/ukol-03.md
from math import ceil


def phone_number_validator(phone_number):
    phone_number=phone_number.replace(" ","")
    if (len(phone_number) == 9 or 
        len(phone_number) == 13 and 
        phone_number[0:4]=="+420"):
        return True
    else:
        print ("Telefonní číslo není platné.")
        return False

def price_per_message(message):
    number_of_messages=ceil(len(message)/180)
    print (f"Cena za tvou zprávu je {number_of_messages*3} Kč.")

phone_number=input("Zadej telefonní číslo: ")
phone_number_validator(phone_number)
if phone_number_validator==True:
    message=input("Tvoje zpráva: ")
    price_per_message(message)