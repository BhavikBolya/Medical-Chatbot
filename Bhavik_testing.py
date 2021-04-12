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


# import pandas as pd
# import spacy

# nlp = spacy.load('en_core_web_md')

# def get_sentence_vectors(text, nlp):

#     # get tokens for each word in sentence
#     embedding = nlp(text).vector.tolist()

#     return embedding

# symptom_df = pd.read_csv('Symptoms.csv')

# symptom_df['embedding'] = symptom_df.apply(lambda row: get_sentence_vectors(row['symptom_name'], nlp), axis = 1)
# print(symptom_df)



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from diagnose import encode_symptom, create_illness_vector, get_diagnosis


class ActionDiagnoseSymptoms(Action):

    def name(self) -> Text:
        return "action_diagnose_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        symptoms = tracker.get_slot("symptom")

        # encode each symptom
        encoded_symptoms = [encode_symptom(symptom) for symptom in symptoms]

        # create a binary vector of symptoms to compare to each each documented illnedd
        illness_vector = create_illness_vector(encoded_symptoms)

        # perform diagnosis
        diagnosis_string = get_diagnosis(illness_vector)

        dispatcher.utter_message(text=diagnosis_string)