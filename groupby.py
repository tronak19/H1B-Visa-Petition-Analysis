import numpy as np
import pandas as pd
import sklearn as sk
import pickle

df = pd.read_csv("h1b_kaggle.csv")
df = df.rename(columns={'Unnamed: 0': 'ID'})
df['FULL_TIME_POSITION'] = np.where(df['FULL_TIME_POSITION']=="Y",1,0)
df = df.drop(['lon', 'lat'], axis=1)
df = df.dropna(subset=['JOB_TITLE'])
df['YEAR'] = df['YEAR'].astype(int)
df = df.loc[df['CASE_STATUS'] == 'CERTIFIED']
df = df.drop(['CASE_STATUS'], axis=1)
df = df.drop(['ID'], axis=1)
df = df.reset_index(drop=True)

grouped_data = df.groupby('JOB_TITLE')
print(list(grouped_data))

with open("grouped_data.pkl", "wb") as f:
    pickle.dump(grouped_data, f)