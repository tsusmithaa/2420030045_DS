import pandas as pd 
data= {1,2,3,10,20,30}
df=pd.DataFrame(data)
print(df)

data={'Name':['AA','BB'],'Age':[20,30]}
df=pd.DataFrame(data)
print(df)

df.to_csv('sample.csv',index=True)

