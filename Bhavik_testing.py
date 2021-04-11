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


# import pandas as pd
# df = pd.read_csv('Data\Training.csv')
# l1 = ['fever', 'cold', '']
# for col in df.columns:
#     for i in l1:
#         if col == i:
#             df = df.loc[df[col] == 1]
# print(df['prognosis'])

# Program to measure the similarity between
# two sentences using cosine similarity.


# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# # X = input("Enter first string: ").lower()
# # Y = input("Enter second string: ").lower()
# X ="fever"
# Y ="high fever"

# # tokenization
# X_list = word_tokenize(X)
# Y_list = word_tokenize(Y)

# # sw contains the list of stopwords
# sw = stopwords.words('english')
# l1 =[];l2 =[]

# # remove stop words from the string
# X_set = {w for w in X_list if not w in sw}
# Y_set = {w for w in Y_list if not w in sw}

# # form a set containing keywords of both strings
# rvector = X_set.union(Y_set)
# for w in rvector:
# 	if w in X_set: l1.append(1) # create a vector
# 	else: l1.append(0)
# 	if w in Y_set: l2.append(1)
# 	else: l2.append(0)
# c = 0

# # cosine formula
# for i in range(len(rvector)):
# 		c+= l1[i]*l2[i]
# cosine = c / float((sum(l1)*sum(l2))**0.5)
# print("similarity: ", cosine)


import pandas as pd
import spacy

nlp = spacy.load('en_core_web_md')

def get_sentence_vectors(text, nlp):

    # get tokens for each word in sentence
    embedding = nlp(text).vector.tolist()

    return embedding

symptom_df = pd.read_csv('Symptoms.csv')

symptom_df['embedding'] = symptom_df.apply(lambda row: get_sentence_vectors(row['symptom_name'], nlp), axis = 1)
print(symptom_df)





# list of illness
illnesses = list(symptom_df['symptom_name'])

# list we will use to store our illness vectors
symptom_vectors = []

for illness in illnesses:
    illness_symptoms = list(symptom_df.loc[symptom_df["symptom_name"]==illness, 'symptom_name'])
    symptom_df["related_to_illness"] = 0
    symptom_df.loc[symptom_df["symptom_name"].isin(illness_symptoms), "related_to_illness"] = 1
    
    
    symptom_vectors.append(list(symptom_df["related_to_illness"]))
    
diagnosis_data = pd.DataFrame({"illness":illnesses,
                              "illness_vector": symptom_vectors})
print(diagnosis_data)