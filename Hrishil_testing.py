import pandas as pd
import spacy

nlp = spacy.load('en_core_web_md')


def get_sentence_vectors(text, nlp):

    # get tokens for each word in sentence
    embedding = nlp(text).vector.tolist()

    return embedding


symptom_df = pd.read_csv('Symptoms.csv')

symptom_df['symtom_vector'] = symptom_df.apply(
    lambda row: get_sentence_vectors(row['symptom'], nlp), axis=1)

symptom_df.to_csv("Symptoms.csv")
