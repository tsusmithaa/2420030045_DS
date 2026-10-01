import pandas as pd

data={'apples':[3, 2, 0, 1], 'oranges':[0, 3, 7, 2]}
df=pd.DataFrame(data)
print(df)


df=pd.DataFrame(data, index=['Ahmad', 'Ali', 'Lily', 'David'])
print (df)


print(df.loc['Ahmad'])

#read dataset
df=pd.read_csv('Iris.csv')
print(df)

print(df.tail(10))
print(df.head(10))

dup_df=pd.concat([df, df])
print(dup_df.shape)
dup_df=dup_df.drop_duplicates()
print(dup_df.shape)

print(df.describe())

