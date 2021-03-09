import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

df = pd.read_csv('Data/Testing.csv')

train_size = int(len(df)*0.70)
test_size = len(df) - train_size
train_data = df[:train_size]
test_data = df[train_size:]

y_tr = train_data.iloc[:,-1]
X_tr = train_data.iloc[:,:-1]

X_test = test_data.iloc[:,:-1]
y_test = test_data.iloc[:,-1]


LR = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(X_tr, y_tr)
print(LR.predict(X_test))
one = round(LR.score(X_test,y_test), 4)

SVM = svm.SVC(decision_function_shape="ovo").fit(X_tr, y_tr)
SVM.predict(X_test)
two = round(SVM.score(X_test, y_test), 4)

RF = RandomForestClassifier(n_estimators=1000, max_depth=10, random_state=0).fit(X_tr, y_tr)
RF.predict(X_test)
three = round(RF.score(X_test, y_test), 4)

NN = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(150, 10), random_state=1).fit(X_tr, y_tr)
NN.predict(X_test)
four = round(NN.score(X_test, y_test), 4)

print(one)
print(two)
print(three)
print(four)