import matplotlib.pyplot as plt
import pandas as pd

Allsongsdataframe = pd.read_csv("mp3tag - mp3tag.csv.csv")
Top100dataframe = pd.read_csv("Most listened to music - Sheet1.csv")

print(Allsongsdataframe.head())
print("\n---------------------", end='\n')
print(Top100dataframe.head())
print("\n---------------------", end='\n')



Allsongsdataframe = Allsongsdataframe.loc[:,"Genre"]
Top100dataframe = Top100dataframe.loc[:, "Genre"]

print(Allsongsdataframe.head())
print("\n---------------------", end='\n')
print(Top100dataframe.head())
print("\n---------------------", end='\n')


print(Allsongsdataframe.value_counts())
print(Top100dataframe.value_counts())

listofGenres = Allsongsdataframe.value_counts.index.tolist()
print(listofGenres)
