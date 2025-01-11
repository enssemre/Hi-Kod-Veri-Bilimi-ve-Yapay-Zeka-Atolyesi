#Ödev 1
ogrenci_notlari = {"Enes": {"Matematik": 95, "Fizik": 80, "Kimya": 60},
                   "Mehmet": {"Matematik": 70, "Fizik": 40, "Kimya": 20},
                   "Ali": {"Matematik": 60, "Fizik": 50, "Kimya": 100}}
isim=input("Öğrencinin adını giriniz: ")
ders=input("Öğrencinin öğrenmek istedğiniz dersin adını giriniz: ")
print(f"{isim} isimli öğrencinin {ders} dersinden aldığı not: {ogrenci_notlari[isim][ders]}")
#%%
#Ödev 2
ogrenci_notlari_2 = {}
ogrenci_notlari_2["Enes"] = {"Matematik": 95, "Fizik": 80, "Kimya": 60}
ogrenci_notlari_2["Mehmet"] = {"Matematik": 70, "Fizik": 40, "Kimya": 20}
ogrenci_notlari_2["Ali"] = {"Matematik": 60, "Fizik": 50, "Kimya": 100}
cikis_karari = True
while cikis_karari:
    istek = input("Ne yapmak istersiniz? (Not sorgulama: 1, Not değitirme: 2, Yeni öğrenci ekleme 3, Çıkış: q)")
    if istek == "1":
        isim = input("Öğrencinin adını giriniz: ")
        ders = input("Öğrencinin öğrenmek istedğiniz dersin adını giriniz: ")
        print(f"{isim} isimli öğrencinin {ders} dersinden aldığı not: {ogrenci_notlari_2[isim][ders]}")
    elif istek == "2":
        isim = input("Öğrencinin adını giriniz:")
        ders = input("Öğrencinin notunu değiştirmek istediğiniz dersin adını giriniz:")
        notu = int(input("Öğrencinin aldığı notu giriniz:"))
        ogrenci_notlari_2[isim][ders] = notu
        print("Not değiştirme işlemi başarılı")
    elif istek == "3":
        isim = input("Öğrencinin adını giriniz:")
        matematik = int(input("Öğrencinin matematik notunu giriniz:"))
        fizik = int(input("Öğrencinin fizik notunu giriniz:"))
        kimya = int(input("Öğrencinin kimya notunu giriniz:"))
        ogrenci_notlari_2[isim] = {"Matematik": matematik, "Fizik": fizik, "Kimya": kimya}
        print("Öğrenci ekleme işlemi başarılı")
    elif istek == "q":
        cikis_karari = False
    else:
        print("Hatalı giriş yaptınız. Lütfen tekrar deneyiniz.")