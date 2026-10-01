import pandas as pd
import seaborn as sns

#tips
tips = sns.load_dataset('tips')
print(tips.head())

#iris
iris = sns.load_dataset('iris')
print(iris.head())

#titanic
titanic = sns.load_dataset('titanic')
print(titanic.head())

#Define the problem:
#predict whether a passenger survied the titanic distaster based on feature
objective="Classification:Survived (Yes/No)"
sucess_criteria="Accuracy of the model"


df = sns.load_dataset('titanic')
print("Data shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe())


#handle missing values
df['age'] = df['age'].fillna(df['age'].mean())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
df.drop_duplicates(inplace=True)
df = pd.get_dummies(df, columns=['sex', 'embarked'], drop_first=True)
df['FamilySize'] = df['sibsp'] + df['parch']


dff=pd.read_csv('student.csv')
print("Data shape:", dff.shape)
print(dff.head())
dff.drop_duplicates(inplace=True)
print("Data shape after removing duplicates:", dff.shape)
#handle missing values
dff['math score'] = dff['math score'].fillna(dff['math score'].mean())


