baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
balik=input("Zadej kod baliku: ")
if balik in baliky:
    if baliky[balik]:
        print ("Balík byl předán kurýrovi.")
    else:
        print ("Balík zatím nebyl předán kurýrovi.")
else:
    print ("Balík nebyl nalezen")
