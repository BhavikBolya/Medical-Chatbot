import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize


word1 = input()
word = word_tokenize(word1)
print(word)
stopwords = stopwords.words("english")
clean = []
for w in word:
    if w not in stopwords:
        clean.append(w)

print(clean)
print("\n")
print(len(clean))