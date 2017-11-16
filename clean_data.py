import numpy as np
import pandas as pd
import sklearn as sk
import pickle

df = pd.read_csv("h1b_kaggle.csv")
df.dropna()
df = df.drop(['lon', 'lat'], axis=1)
df = df.loc[df['CASE_STATUS'] == 'CERTIFIED']
df.dropna(subset=['JOB_TITLE'], inplace = True)
soc_null = df[pd.isnull(df['SOC_NAME'])]
print("soc_null shape = ", soc_null.shape)
soc_not_null = df[pd.notnull(df['SOC_NAME'])]
print("soc_not_null shape = ", soc_not_null.shape)
job_titles_list = soc_null['JOB_TITLE'].unique()
job_titles_list
print("soc_null unique job_titles_list = ", len(job_titles_list))
train_df = df.loc[df['YEAR'] != 2016]
train_df
print("train_df shape = ", train_df.shape)
test_df = df.loc[df['YEAR'] == 2016]
test_df
print("test_df shape = ", test_df.shape)
# grouped_data = df.groupby('JOB_TITLE')
# print(list(grouped_data))
count=0
for index1, row1 in soc_null.iterrows():
    for index2, row2 in soc_not_null.iterrows():
         if row1['JOB_TITLE'] == row2['JOB_TITLE']:
                soc_null.set_value(index1,'SOC_NAME',row2['SOC_NAME'])
                print(row2['SOC_NAME'])
                count+=1
                print("count = ", count)
                break

df.to_pickle('df.pkl')

df = df.rename(columns={'Unnamed: 0': 'Serial_Number'})
df.drop(['Serial_Number'], axis=1)
df = df.reset_index(drop=True)
print(df)
# df = df.set_index('Serial_Number')
df.to_pickle('clean_df.pkl')