import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=sns.load_dataset('titanic')

#histogram of age
sns.histplot(df['age'], bins=30, kde=True)
plt.title('Age Distribution')
#plt.show()


dff=pd.read_csv('student.csv')
sns.histplot(dff['Attendance'], bins=30, kde=True)
plt.title('Attendance Distribution')
#plt.show()


#heatmap
corr_matrix = df.corr(numeric_only=True)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


#student csv
corr=dff.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap for Student Data')
plt.show()