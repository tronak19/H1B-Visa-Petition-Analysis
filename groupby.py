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

# grouped_data = df.groupby('JOB_TITLE')
# print(list(grouped_data))

# with open("grouped_data.pkl", "wb") as f:
# 	pickle.dump(grouped_data, f)

df = df.dropna()
df = df.reset_index(drop=True)
unique_soc_name_list = df['SOC_NAME'].unique()
mapping_dict={}
for i in range(len(unique_soc_name_list)):
    temp_df = df.loc[df['SOC_NAME'] == unique_soc_name_list[i]]
    temp_list = temp_df['JOB_TITLE'].unique()
    mapping_dict[unique_soc_name_list[i]] = temp_list
with open("mapping_dict.pkl", "wb") as f:
	pickle.dump(mapping_dict, f)

import pprint
pprint.pprint(mapping_dict)