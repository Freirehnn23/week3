yang_benar = input("Masukan Suhu Anda")
try:
    a = int(yang_benar)
    if a >= 38 :
        print ("Anda Demam Segera Minum Obat")
    elif a <=38:
        print("Anda Kelelahan Segera Istirahat")
except :
    print ("Input Anda Salah ")