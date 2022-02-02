import csv
import pandas as pd

df = pd.read_csv("total_stars.csv")
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
final_data = df.dropna()
df.reset_index(drop = True, inplace = True)
final_data.to_csv("final_data.csv")