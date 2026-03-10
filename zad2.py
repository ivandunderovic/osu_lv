try:
    unos = input("Unesite ocjenu (između 0.0 i 1.0): ")
    broj = float(unos)

    if broj < 0.0 or broj > 1.0:
        print("Greška: Broj mora biti u intervalu od 0.0 do 1.0.")
    elif broj >= 0.9:
        print("Ocjena: A")
    elif broj >= 0.8:
        print("Ocjena: B")
    elif broj >= 0.7:
        print("Ocjena: C")
    elif broj >= 0.6:
        print("Ocjena: D")
    else:
        print("Ocjena: F")

except ValueError:
    print("Niste unijeli ispravan broj.")