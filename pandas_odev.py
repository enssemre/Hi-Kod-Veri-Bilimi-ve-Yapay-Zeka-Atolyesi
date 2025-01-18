import pandas as pd
sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
         "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
         "Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

#Soru1
df = pd.DataFrame(sozluk)
print(df)

#Soru2
print(df.loc[2, "Kategori"])
print(df.loc[2, "Ürün"])
print(df.iloc[4:])
print(df.loc[1:6, "Ürün"])

#Soru 3
df_giyim = df[df["Kategori"]=="Giyim"]
df_ayakkabı = df[df["Kategori"]=="Ayakkabı"]
df_aksesuar = df[df["Kategori"]=="Aksesuar"]

print(df_giyim)
print(df_ayakkabı)
print(df_aksesuar)

#Soru4
df_giyim_fiyat = df_giyim[df_giyim["Fiyat"]>300]
df_ayakkabı_fiyat = df_ayakkabı[df_ayakkabı["Fiyat"]>600]
df_aksesuar_fiyat = df_aksesuar[df_aksesuar["Fiyat"]>100]

print(df_giyim_fiyat)
print(df_ayakkabı_fiyat)
print(df_aksesuar_fiyat)