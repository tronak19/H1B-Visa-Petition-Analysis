import numpy as np
import pandas as pd
import sklearn as sk
import pickle

df = pd.read_csv("h1b_kaggle.csv")
df.dropna()
df = df.drop(['lon', 'lat'], axis=1)
df = df.loc[df['CASE_STATUS'] == 'CERTIFIED']
df.dropna(subset=['JOB_TITLE'], inplace = True)

df = df.rename(columns={'Unnamed: 0': 'Serial_Number'})
df.drop(['Serial_Number'], axis=1)
df = df.reset_index(drop=True)
df = df.set_index('Serial_Number')
data = df.groupby('JOB_TITLE')
print(list(data))

with open("groupby2.pkl", "wb") as f:
    pickle.dump(data, f)