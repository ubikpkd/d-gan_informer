import pandas as pd
import random

df_raw = pd.read_csv('./WTH.csv')
df_raw.fillna(0.0,inplace=True)

zero = 0
count = 0
for idx, row in df_raw.iterrows():
    for i in range(1,13):
        if row[i] == 0.0:
            zero += 1
        count += 1
print("zero is %d, count is %d, zero/count is %f" %(zero,count,zero/count))