# input a, b dan c
a = input("Masukkan bilangan pertama: ")
b = input("Masukkan bilangan kedua: ")
c = input("Masukkan bilangan ketiga: ")

# secara berurutan tulis kriteria untuk a, b, dan c=
try:
    bilangan_benar = int(a, b, c)

    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    elif c > a and c > b:
        print("Terbesar: ", c)
except:
    print("Input Anda Salah")