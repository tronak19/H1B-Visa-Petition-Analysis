import numpy as np
import pandas as pd
import sklearn as sk
import pickle

with open("grouped_data.pkl", "rb") as f:
	grouped_data = pickle.load(f)
grouped_data
print(len(list(grouped_data)))