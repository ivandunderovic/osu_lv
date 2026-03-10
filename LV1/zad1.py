def total_income(radni_sati: float, satnica:float):
    return satnica*radni_sati

radni_sati = float(input("Unesite broj radnih sati: "))
satnica = float(input("Unesite koliko ste plaćeni po satu (€): "))

ukupno = total_income(radni_sati,satnica)

print("Ukupna zarada iznosi:", ukupno, "€")
