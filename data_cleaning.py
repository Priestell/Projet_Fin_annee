import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/hotel.csv")
del(df["Unnamed: 0"])
print(df.describe)
print(df.columns)