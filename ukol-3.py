#https://github.com/andywaltlova/python-1-podzim-2022/blob/master/ukoly/ukol-03.md
from dataclasses import replace
from math import ceil

phone_number=input ("Zadej telefonní číslo: ")
phone_number=phone_number.replace(" ","")
def phone_number_validator (phone_number):
    if len(phone_number) == 9 or len(phone_number) == 13 and phone_number[0:4]=="+420":
        return phone_number==True
    else:
        print ("Telefonní číslo není platné.")
        exit()
phone_number_validator (phone_number)

message=input ("Tvoje zpráva: ")
number_of_messages=ceil(len(message)/180)
def price_per_message (message):
    print (f"Cena za tvou zprávu je {number_of_messages*3} Kč.")
price_per_message(message)