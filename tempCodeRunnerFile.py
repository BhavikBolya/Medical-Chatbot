import pandas as pd
df =  pd.read_csv('Data\Training.csv')
l1 = [1,0,0,0,1,1,1,0]
for col in df.columns:
    for i in l1:
        if col==i:
            df = df.loc[df[col]==1]
print(df['prognosis'])