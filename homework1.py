# 1. soru #
x=3
x=float(x)
print(type(x))
#%%
y=4.5
y=int(y)
print(type(y))
#%%
z='8'
z=int(z)
print(type(z))
#%%
a='12'
a=float(a)
print(type(a))
#%%
b='46.8'
b=int(float(b))
print(type(b))
#%%
# 2. soru #
Enes=20
Asude=22
Kemal=17
print(Enes>Asude)
print(Kemal<Asude)
print(Enes==Kemal)
print(Enes!=Asude)
# %%
# 3. soru #
number1=int(input('Bir sayi giriniz: '))
number2=int(input('Bir sayi daha giriniz: '))
toplam=number1+number2
cikarma=number1-number2
carpma=number1*number2
bolme=number1/number2
print('Toplam: ',toplam)
print('Cikarma: ',cikarma)
print('Carpma: ',carpma)
print('Bolme: ',bolme)
# %%
# 4. soru #
isim=input('Isminizi giriniz: ')
yas=int(input('Yasinizi giriniz: '))
sehir=input('Sehrinizi giriniz: ')
meslek=input('Mesleginizi giriniz: ')
print('Isminiz: ',isim)
print('Yasiniz: ',yas)
print('Sehriniz: ',sehir)
print('Mesleginiz: ',meslek)
# %%
# 5. soru #
ifade="Hi-Kod Veri Bilimi Atöyesi"
parcala=ifade.split()
print(parcala)
buyukharf=ifade.upper()
print(buyukharf)
kucukharf=ifade.lower()
print(kucukharf)
# %%
sayi="0123456789"
cift=sayi[0::2]
print(cift)
tek=sayi[1::2]
print(tek)