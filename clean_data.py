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

soc_null = df[pd.isnull(df['SOC_NAME'])]
print("soc_null shape = ", soc_null.shape)

soc_not_null = df[pd.notnull(df['SOC_NAME'])]
print("soc_not_null shape = ", soc_not_null.shape)

count=0
for index1, row1 in soc_null.iterrows():
	flag=0
	for index2, row2 in soc_not_null.iterrows():
		if row1['JOB_TITLE'] == row2['JOB_TITLE']:
				soc_null.set_value(index1,'SOC_NAME',row2['SOC_NAME'])
				print(row2['SOC_NAME'])
				count+=1
				print("count = ", count)
				flag=1
				break
	if flag==0:
		soc_null.set_value(index1,'SOC_NAME',"UNDEFINED")

soc_null.to_pickle('soc_null_df.pkl')