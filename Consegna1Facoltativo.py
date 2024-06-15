from math import pi

dizionarioforme = {1:"Quadrato", 2:"Cerchio", 3:"Rettangolo"}
lista = [1,2,3]

while len(lista) > 0:
    print("Le figure geometriche sono:\n")
    for i in dizionarioforme.keys ():
        if (i in lista):
            print(f"{i}. {dizionarioforme[i]}")

    scelta = float(input("\n"))
    if (scelta == 1):
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        perimetro = lato * 4
        print(f"Il perimetro del quadrato è: {perimetro}")
    elif (scelta == 2):
        raggio = float(input("Inserisci il raggio del cerchio: "))
        circonferenza = 2 * pi * raggio
        print(f"La circonferenza del cerchio è: {circonferenza}")
    elif (scelta == 3):
        base = float(input("Inserisci la lunghezza della base del rettangolo: "))
        altezza = float(input("Inserisci la lunghezza dell'altezza del rettangolo: "))
        perimetro = 2 * (base + altezza)
        print(f"Il perimetro del rettangolo è: {perimetro}")
    else:
        print("Scelta non valida. Per favore, seleziona un'opzione valida.")
        
    lista.remove (scelta)