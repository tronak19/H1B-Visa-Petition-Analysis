import numpy as np
import pandas as pd
import sklearn as sk
import pickle

with open("groupby.pkl", "rb") as f:
	grouped_data = pickle.load(f)
grouped_data
print(list(grouped_data))