#Ödev 1
liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
print(liste[3])
print(liste[-3])
print(liste[-1])
print(liste[2:6])
print(liste[4:])
#%%
#Ödev 2
liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
yeni_liste = []
for i in liste:
    if type(i) == str:
        yeni_liste.append(i)
print(yeni_liste)
#%%
#Ödev 3
meyveler = ["elma", "armut", "muz", "çilek", "kivi", "karpuz", "kavun", "kiraz", "erik", "üzüm"]
for index, meyve in enumerate(meyveler):
    print(f"{index+1}, indexte bulunan meyve: {meyve}")