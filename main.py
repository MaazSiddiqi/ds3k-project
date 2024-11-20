import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

# Load the dataset
dataset_name = "mock_data.csv"

df = pd.read_csv(dataset_name)

# TODO: clean data
df.head()
