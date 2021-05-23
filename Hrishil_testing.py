import pandas as pd
import spacy
import random
import re
nlp = spacy.load('en_core_web_md')


def get_sentence_vectors(text, nlp):

    # get tokens for each word in sentence
    embedding = nlp(text).vector.tolist()

    return embedding


symptom_df = pd.read_csv('Symptoms.csv')

symptom_df['symptom_vector'] = symptom_df.apply(
    lambda row: get_sentence_vectors(row['symptom'], nlp), axis=1)

symptom_df.to_pickle('symptoms90.pkl')


# number_of_symptoms = [1, 2, 3, 4]
start_of_description = [
    "I have",
    "I'm suffering from",
    "I have really bad",
    "My symptoms are",
    "For the last few days I have had"
]

# get some examples of users describing different numbers of syptoms
for symptons_count in range(1,60):
    
    # make 100 examples of each number of symptoms
    for ex in range(1, 101):
    
        description_beginning = random.choice(start_of_description)
        
        # collect some random symtpoms
        symptom_1 = symptom_df['symptom'].sample(1).iloc[0].lower()
        symptom_2 = symptom_df['symptom'].sample(1).iloc[0].lower()
        symptom_3 = symptom_df['symptom'].sample(1).iloc[0].lower()
        symptom_4 = symptom_df['symptom'].sample(1).iloc[0].lower()
        
        symptoms = [symptom_1, symptom_2, symptom_3, symptom_4]
        # print(symptoms)
        symptoms_entity = []
        
        # remove parenthases from symptoms and add nessecary entitiy tags to symptoms
        for symptom in symptoms:
            symptom = re.sub(r"\([^)]+\)", "", symptom).strip()
            symptom = f"[{symptom}](Symptom)"
            symptoms_entity.append(symptom)
            
        symptom_1 = symptoms_entity[0]
        symptom_2 = symptoms_entity[1]
        symptom_3 = symptoms_entity[2]
        symptom_4 = symptoms_entity[3]
        
        # create the training sample string
        if symptons_count == 1:
            
            symptom_string = f"- {description_beginning} {symptom_1}"
            
        if symptons_count == 2:
            
            symptom_string = f"- {description_beginning} {symptom_1} and {symptom_2}"
            
        if symptons_count == 3:
            
            symptom_string = f"- {description_beginning} {symptom_1}, {symptom_2}, and {symptom_3}"
            
        if symptons_count == 4:
            
            symptom_string = f"- {description_beginning} {symptom_1}, {symptom_2}, {symptom_3}, {symptom_4}"
        
        print(symptom_string)