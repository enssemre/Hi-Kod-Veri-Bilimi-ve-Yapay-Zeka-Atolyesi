#Ödev 1
def daire_alan_hesapla(yaricap, pi):
    return pi * yaricap ** 2

yaricap=(int(input("Yarıçapı giriniz: ")))
pi=(float(input("Pi sayısını giriniz: ")))
alan=daire_alan_hesapla(yaricap, pi)
print(f"Dairenin alanı: {alan}")
#%%
#Ödev 2
def faktoriyel(sayi):
    if sayi==1 or sayi==0:
        return 1
    else:
        for i in range (1, sayi):
            sayi*=i
    return sayi

sayi=(int(input("Faktoriyelini almak istediğiniz sayıyı giriniz: ")))
if sayi<0:
    print("Negatif sayıların faktoriyeli hesaplanamaz.")
else:
    faktoriyel_sonuc=faktoriyel(sayi)
    print(format(faktoriyel_sonuc))
#%%
#Ödev 3
def yas_hesapla(dogum_yili):
    return 2025-dogum_yili

dogum_yili=(int(input("Doğum yılınızı giriniz: ")))
yas=yas_hesapla(dogum_yili)
print(f"Yaşınız: {yas}")
#%%
#Ödev 4
def emeklilik_kontrol(yas, isim):
    if yas>=65:
        print("Emekli oldunuz.")
    else:
        print(f"{isim}, emekli olmanıza {65-yas} yıl kaldı.")

def yas_hesapla(dogum_yili, isim):
    yas=2025-dogum_yili
    emeklilik_kontrol(yas, isim)

dogum_yili=(int(input("Doğum yılınızı giriniz: ")))
isim=(input("Adınızı giriniz: "))
yas=yas_hesapla(dogum_yili, isim)