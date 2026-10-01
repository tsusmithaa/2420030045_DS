import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [23, 30, np.nan, 25, 40],
    'Department': ['HR', 'IT', 'Finance', np.nan, 'HR']
})
print(df)

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Department'] = df['Department'].fillna(df['Department'].mode()[0])
print(df)


print()

#2 ffill
df = pd.DataFrame({'Age': [25, 30, np.nan, 40], 'Department': ['HR', 'IT', np.nan   , 'Marketing']})
print(df)
df_ffill = df.copy()
df_ffill.ffill(inplace=True)
print(df_ffill)

print()
#3 bfill defination: 
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40],
    'Department': ['HR', 'IT', np.nan, 'Marketing']
})
print(df)
df_bfill = df.copy()
df_bfill.bfill(inplace=True)
print(df_bfill)
print()



#4 rows, cols
df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40],
    'Department': ['HR', 'IT', np.nan, 'Marketing']
})
print(df)
df_drop_rows = df.dropna()
print("After dropping rows:", df_drop_rows)
df_drop_cols=df.dropna(axis=1)
print("After dropping columns:", df_drop_cols)
df_drop_cols=df.dropna(axis=0)
print("After dropping columns:", df_drop_cols)

#5 drop duplicates
df= pd.DataFrame({
    'ID': [1, 2, 3, 4, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'David'],
    'Age': [25, 30, np.nan, 40, 40]
})
df_exact = df.drop_duplicates()
print("\nAfter dropping duplicates:\n", df_exact)

#6 subset based removal
#remove duplicates based on 'ID' column
#remove duplicates based on selcted columns
df=pd.DataFrame({
    'ID': [1, 2, 3, 4, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'David'],
    'Age': [25, 30, np.nan, 40, 40]
})
df_subset_id = df.drop_duplicates(subset=['ID'])
print("\nAfter subset based removal(id):\n", df_subset_id)
df_subset_name=df.drop_duplicates(subset=['Name'])
print("\nAfter subset based removal(name):\n", df_subset_name)

#7 date time
df=pd.DataFrame({
    'Date': ['2023-01-01', '2023-02-15', '2023-03-10']
})
print("\nOriginal DataFrame:\n", df)
df['Date']=pd.to_datetime(df['Date'],errors='coerce').dt.strftime('%Y-%m-%d')
print(df)


#8 lowercase, uppercase
df=pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie']})
df['Name_lowercase']=df['Name'].str.lower()
df['Name_uppercase']=df['Name'].str.upper()
print(df)