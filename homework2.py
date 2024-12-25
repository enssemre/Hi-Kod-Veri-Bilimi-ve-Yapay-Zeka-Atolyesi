#Ödev 1
maas=int(input("Maaşinizi giriniz:"))
if maas>0:
    if maas<=10000:
        yeni_maas=maas-(maas*0.05)
        print(f"Yeni maaşiniz: {yeni_maas}")
    elif maas<=25000:
        yeni_maas=maas-(maas*0.10)
        print(f"Yeni maaşiniz: {yeni_maas}")
    elif maas<=45000:
        yeni_maas=maas-(maas*0.25)
        print(f"Yeni maaşiniz: {yeni_maas}")
    else:
        yeni_maas=maas-(maas*0.30)
        print(f"Yeni maaşiniz: {yeni_maas}")
else:
    print("Lütfen geçerli bir maaş giriniz.")
#%%
#Ödev 2
kullanici_adi=input("Kullanici adinizi giriniz:")
sifre=input("Sifrenizi giriniz:")
while len(sifre)<6:
    print("Sifreniz en az 6 karakter olmalidir.")
    sifre=input("Sifrenizi giriniz:")
print("Kullanici adiniz ve sifreniz kaydedildi.")
# %%
#Ödev 3
kullanici_adi=input("Kullanici adinizi giriniz:")
sifre=input("Sifrenizi giriniz:")
while (len(sifre)<6 or len(sifre)>10):
    print("Lütfen giridiğiniz 5 haneden az 10 haneden fazla olmsın!")
    sifre=input("Sifrenizi giriniz:")
print("Hesabınız oluşturuldu.")

#Ödev 4
giris_hakki=3
while giris_hakki>0:
    giris_sifre=input("Sifrenizi giriniz:")
    if giris_sifre==sifre:
        print("Giriş yapıldı.")
        break
    else:
        giris_hakki-=1
        print(f"Yanlış şifre girildi! Kalan giriş hakkı: {giris_hakki}")
