def zmena_znamky(stara_hodnota):
    if stara_hodnota==1:
        return "A"
    elif stara_hodnota==2:
        return "B"
    elif stara_hodnota==3:
        return "C"
    elif stara_hodnota==4:
        return "D"
    elif stara_hodnota==5:
        return "F"
    else:
        return "Neočekávaná známka."

with open("znamky.csv", encoding='utf-8') as vstup:
    radky=vstup.readlines()

radky = [radek.split(',') for radek in radky]

for i, radek in enumerate(radky):
    if i > 0:
        for j, sloupec in enumerate(radek):
            if j > 1:
                # pro pochopeni postupu
                # radek[j]=int(sloupec)
                # zmena_znamky(radek[j])
                radek[j]=zmena_znamky(int(sloupec))
    else:
        radek[-1]=radek[-1].replace("\n","")

nove_radky=[]
for radek in radky:
    nove_radky.append(",".join(radek)+"\n")
    
with open('nove_znamky.csv', mode='w', encoding='utf-8') as vystup:
    vystup.writelines(nove_radky)
