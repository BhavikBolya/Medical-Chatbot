# import pandas as pd
# import numpy as np
# import sklearn as sk
# from sklearn.linear_model import LogisticRegression
# from sklearn import svm
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.neural_network import MLPClassifier

# df1 = pd.read_csv('Data/Testing.csv')
# df2 = pd.read_csv('Data/Testing.csv')

# # df = pd.read_csv('Data/dataset.csv')

# # train_size = int(len(df)*0.70)
# # test_size = len(df) - train_size
# # train_data = df[:train_size]
# # test_data = df[train_size:]

# # y_train = train_data.iloc[:, -1]
# # X_train = train_data.iloc[:, :-1]

# # X_test = test_data.iloc[:, :-1]
# # y_test = test_data.iloc[:, -1]

# y_train = df1.iloc[:,-1]
# X_train = df1.iloc[:,:-1]

# X_test = df2.iloc[:,:-1]
# y_test = df2.iloc[:,-1]


# LR = LogisticRegression(random_state=0, solver='lbfgs',
#                         multi_class='multinomial').fit(X_train, y_train)
# print(LR.predict(X_test))
# one = LR.score(X_test, y_test)

# SVM = svm.SVC(decision_function_shape="ovo").fit(X_train, y_train)
# SVM.predict(X_test)
# two = SVM.score(X_test, y_test)

# RF = RandomForestClassifier(
#     n_estimators=1000, max_depth=10, random_state=0).fit(X_train, y_train)
# RF.predict(X_test)
# three = RF.score(X_test, y_test)

# NN = MLPClassifier(solver='lbfgs', alpha=1e-5,
#                    hidden_layer_sizes=(150, 10), random_state=1).fit(X_train, y_train)
# NN.predict(X_test)
# four = NN.score(X_test, y_test)

# print(one)
# print(two)
# print(three)
# print(four)
