yang_benar = input("Masukan Satu Bilangan: ")
try:
    bilangan = int(yang_benar)
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")
except:
    print("Masukan Dengan Benar")