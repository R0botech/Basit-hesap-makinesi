print(""" 
    1- Toplama
    2- Çıkarma
    3- Çarpma
    4- Bölme
    5- Üs alma
""")
islem = int(input("yapılacak işlemi seçiniz: "))

if islem == 1:
    print("Toplama İslemi")
    deger1 = int(input("Lutfen 1. sayi degerini girin: "))
    deger2 = int(input("Lutfen 2. sayi degerini girin: "))

    toplam = deger1 + deger2
    print(f'Islem sonucu: {toplam}')
elif islem == 2:
    deger1 = int(input("Lutfen 1. sayi degerini girin: "))
    deger2 = int(input("Lutfen 2. sayi degerini girin: "))

    fark = deger1 - deger2
    print(f'Islem sonucu: {fark}')

elif islem == 3:
    deger1 = int(input("Lutfen 1. sayi degerini girin: "))
    deger2 = int(input("Lutfen 2. sayi degerini girin: "))

    carp = deger1 * deger2
    print(f'Islem sonucu: {carp}')

elif islem == 4:
    deger1 = int(input("Lutfen 1. sayi degerini girin: "))
    deger2 = int(input("Lutfen 2. sayi degerini girin: "))

    bol = deger1 / deger2
    print(f'Islem sonucu: {bol}')
elif islem == 5:
    deger1 = int(input("Lutfen 1. sayi degerini girin: "))
    deger2 = int(input("Lutfen 2. sayi degerini girin: "))

    us = deger1 ** deger2
    print(f'Islem sonucu: {us}')
else:
    print("GECERSIZ ISLEM")
