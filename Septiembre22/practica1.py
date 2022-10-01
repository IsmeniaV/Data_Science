#https://colab.research.google.com/drive/1aRnmWC7e15slYKzZcYzu8b8f0bix6wi0#scrollTo=oKYhj3glXv_O

from multiprocessing.sharedctypes import Value
import pandas as pd

df = pd.read_csv("data_filt.csv"
           , encoding = 'latin1')

print(df)


print(df["p47t"].sum())

print(df["p47t"].mean())

df2=df[["nivel_ed","p47t"]]
print(df2)

df.columns=['edad', 'nivel_educativo', 'hs_trabajadas', 'calif_ocupacional', 'ingreso_ult_mes']
print(df)

print(df.index)

print(df["calif_ocupacional"].dtype)

print(df["calif_ocupacional"].value_counts())

print(df["nivel_educativo"].value_counts())

print(df.head(20))

print(df.sample(500))

print(df.loc[:,df.columns!="nivel_educativo"])

print(df.sort_values("edad"))

df3=(df["calif_ocupacional"] == "2_Op./No calif.")&(df["edad"] >14)&(df["edad"]<25)
print(df.loc[df3])

print(df.loc[df3].sort_values("edad"))

promIng=(df["ingreso_ult_mes"].mean())
print(promIng)

medHoras=(df["hs_trabajadas"].mean())
print(medHoras)

dfNew=df.loc[(df["ingreso_ult_mes"] > promIng) & (df["hs_trabajadas"] < medHoras)]
print(dfNew)


print(dfNew.index)

print(df.loc[dfNew].median())