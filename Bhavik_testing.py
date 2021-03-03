# import nltk
# from nltk.corpus import stopwords
# from nltk import word_tokenize

# word1 = input()
# word = word_tokenize(word1)
# print(word)
# stopwords = stopwords.words("english")
# clean = []
# for w in word:
#     if w not in stopwords:
#         clean.append(w)

# print(clean)
# print("\n")
# print(len(clean))


import pandas as pd
import numpy as np

df =  pd.read_csv('Data\Training.csv')

l1 = ['prominent_veins_on_calf']

for col in df.columns:
    for i in l1:
        if col==i:
            df = df.loc[df[col]==1]
print(df['prognosis'])