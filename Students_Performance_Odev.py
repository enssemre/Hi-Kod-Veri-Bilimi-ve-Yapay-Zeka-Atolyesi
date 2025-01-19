import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1
df = pd.read_csv("c:/Users/emren/OneDrive/Masaüstü/Kodluyoruz/hi kod 2.0/hikod 2.0 notlari/hikod odevleri/StudentsPerformance.csv")
print(df.head())

#2
print(df["gender"].value_counts())

#3
plt.figure(figsize=(5,7))
sns.histplot(x="gender", data=df)
plt.xlabel("Gender")
plt.ylabel("Numbers Gender")
plt.show()

#4
race = df["race/ethnicity"].value_counts().reset_index()
print(race)

#5
sns.histplot(x="race/ethnicity", data=df)
plt.ylabel("Numbers Group")
plt.show()

#6
education_unique = df["parental level of education"].unique()
print(education_unique)

#7
lunch_unique = df["lunch"].unique()
print(lunch_unique)

#8
lunch = df["lunch"].value_counts()
print(lunch)

#9
group_gender = df.groupby("gender")[["math score", "reading score", "writing score"]].mean().reset_index()
print(group_gender)

#10
group_race = df.groupby("race/ethnicity")[["math score", "reading score", "writing score"]].mean().reset_index()
print(group_race)

#11
group_education = df.groupby("parental level of education")[["math score", "reading score", "writing score"]].mean().reset_index()
print(group_education)

#12
group_lunch = df.groupby("lunch")[["math score", "reading score", "writing score"]].mean().reset_index()
print(group_lunch)

#13
group_test_preparration = df.groupby("test preparation course")[["math score", "reading score", "writing score"]].mean().reset_index()
print(group_test_preparration)