import pandas as pd
import numpy as np

df = pd.read_csv('GG.csv')

train_size = int(len(df)*0.70)
test_size = len(df) - train_size
train_data = df[:train_size]
test_data = df[train_size:]

y_train = train_data.iloc[:,-1]
X_train = train_data.iloc[:,:-1]

print(X_train)
print(y_train)