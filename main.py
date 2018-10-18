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

listofGenres = Allsongsdataframe.value_counts().index.tolist()
listofGenres100 = Top100dataframe.value_counts().index.tolist()
countsofgenre = Allsongsdataframe.value_counts().tolist()
countsofgenre100 = Top100dataframe.value_counts().tolist()
print(countsofgenre, end='\n')
print(countsofgenre100)
print(listofGenres, end="\n")
print(listofGenres100, end="\n")

#Ploting data
