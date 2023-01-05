# Sayı Tahmin Oyunu
print("Sayı Tahmin Oyununa Hoşgeldiniz!")
number=20
player_number=int(input("0 ile 20 arasında bir sayı giriniz: "))
change=3

while True:
    change<3
    if player_number>number:
        change-=1
        print(change,"Hakkınız Kaldı")
        player_number=int(input("Daha küçük bir sayı tahmin edin: "))
    elif player_number<number:
        change-=1
        print(change,"Hakkınız Kaldı")
        player_number=int(input("Daha büyük bir sayı tahmin edin: "))
    if player_number==number:
        print("Tebrikler, Oyunu Kazandınız".center(50,"*"))
        break
    if change==0:
        print("Üzgünüm, Kaybettiniz :(".center(50,"-"))
        break
    