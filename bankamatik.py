
print("1.Bakiye Sorgula / 2.Para Yatır / 3.Para Çek")
bakiye = 1000
while True:
    islemSec = input("İşlem seçiniz: ")
    if islemSec == "1":
        print(f"Bakiyeniz {bakiye} TL")
    elif islemSec == "2":
        yatir = int(input("Miktar Giriniz: "))
        bakiye += yatir
    elif islemSec == "3":
        cek = int(input("Miktar Giriniz: "))
        if bakiye - cek <= -500:
            print("-500 fazla para çekemezsiniz  ")
            continue
        bakiye -= cek
    else:
        print("Yanlış işlem yapıyorsunuz")