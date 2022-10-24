import pandas as pd
import numpy as np

from utils.metrics import metric
from utils.tools import StandardScaler

scaler = StandardScaler()
df_raw = pd.read_csv("./ETTh1.csv")
df_lost = pd.read_csv("./ETTh1_80.csv")
df_mask = pd.read_csv("./ETTh1_80_mask.csv")

for i in range(1, len(df_mask)):
    for j in range(1, len(df_mask.columns)):
        if df_lost.iloc[i][j] == 0.0:
            ave = 0.0
            for a in range(max(0, i-48), i):
                ave += df_raw.iloc[a][j]
            df_lost.iloc[i][j] = ave/(min(48,i))

df_raw = df_raw.iloc[:, 1:]
df_lost = df_lost.iloc[:, 1:]
scaler.fit(df_raw.values)
raw = scaler.transform(df_raw.values)
lost = scaler.transform(df_lost.values)

preds = np.array(lost)
trues = np.array(raw)
preds = preds.reshape(-1, preds.shape[-2], preds.shape[-1])
trues = trues.reshape(-1, trues.shape[-2], trues.shape[-1])

mae, mse, rmse, mape, mspe = metric(preds, trues)
print('imputation\'s mse:{}, mae:{}, rmse:{}'.format(mse, mae, rmse))