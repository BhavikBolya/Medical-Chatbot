import pandas as pd
print(pd.__version__)
df = pd.read_csv("Data/Testing.csv")

prog_list = []
tup_list = []
id_list = []
k = 0
for i in df.itertuples():
    tup = []
    for j in range(1,133):
        tup.append(i[j])
    prog = i[133]
    prog_list.append(prog)
    tup_list.append(tup)
    id_list.append(k)
    k=k+1

dfx = pd.DataFrame()
dfx[None] = id_list
dfx['illness'] = prog_list
dfx['illness_vector'] = tup_list

dfx.to_pickle("Illness.pkl")

df3 = pd.read_csv("Symptoms.csv")
df3.to_pickle("Symptoms_new.pkl")

