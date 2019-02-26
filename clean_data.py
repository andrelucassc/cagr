import pandas as pd

df = pd.read_csv('Dados CAGR.csv',sep='\t',index_col=0)

print(df)

print(df.info())

print(df.head())
