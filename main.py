import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99',"#fcff6b","#ff6ae3","#a5ff69"]
x = np.char.array(listofGenres)
y = np.array(countsofgenre)


percent = 100.*y/y.sum()
patches, texts, = plt.pie(y, colors=colors, startangle=90, radius=1.2)
labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(x, percent)]

for text in texts:
    text.set_color('grey')

# for autotext in autotexts:
#     autotext.set_color('grey')

sort_legend = True
if sort_legend:
    patches, labels, dummy =  zip(*sorted(zip(patches, labels, y),
                                          key=lambda x: x[2],
                                          reverse=True))


plt.legend(patches, labels, loc='center left', bbox_to_anchor=(-0.1, 1.),
           fontsize=8)

# fig1, ax1 = plt.subplots()
# patches, texts, autotexts = ax1.pie(countsofgenre, colors = colors, labels=listofGenres,
#                                     autopct='%1.1f%%', startangle=90)


# ax1.axis('equal')
plt.tight_layout()
plt.show()
