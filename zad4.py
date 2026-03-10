import string

try:
    with open("lv1/song.txt", "r", encoding="utf-8") as file:
        tekst = file.read().lower()

    
    for znak in string.punctuation:
        tekst = tekst.replace(znak, "")


    rijeci = tekst.split()

    brojac = {}

    for rijec in rijeci:
        if rijec in brojac: 
            brojac[rijec] += 1
        else:
            brojac[rijec] = 1

    
    jednom = [rijec for rijec, broj in brojac.items() if broj == 1]

    print(f"Broj riječi koje se pojavljuju samo jednom: {len(jednom)}\n")
    print("Riječi koje se pojavljuju samo jednom:")
    for rijec in jednom:
        print(rijec)

except FileNotFoundError:
    print("Greška: Datoteka 'song.txt' ne postoji.")
