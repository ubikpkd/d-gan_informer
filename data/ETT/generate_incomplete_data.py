import pandas as pd
import random

df_raw = pd.read_csv('./ECL.csv')
df_raw.fillna(0.0,inplace=True)

for idx, row in df_raw.iterrows():
    for i in range(1,322):
        if random.randint(1, 10) <= 5:
            row[i] = 0.0
    df_raw.iloc[idx] = row

df_mask = df_raw.copy()
for idx, row in df_mask.iterrows():
    for i in range(1,322):
        if row[i] != 0.0:
            row[i] = 1.0
    df_mask.iloc[idx] = row

df_raw.to_csv('./ECL_50.csv',index=False)
df_mask.to_csv('./ECL_50_mask.csv',index=False)