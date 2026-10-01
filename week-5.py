import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print("Original Data:")
print(tips.head())

numeric_cols = tips.select_dtypes(include=['float64', 'int64']).columns
scaler_minmax = MinMaxScaler()
tips_normalized = tips.copy()
tips_normalized[numeric_cols] = scaler_minmax.fit_transform(tips[numeric_cols])
print("\nNormalized Data:")
print(tips_normalized.head())   

scaler_standard = StandardScaler()
tips_standardized = tips.copy()
tips_standardized[numeric_cols] = scaler_standard.fit_transform(tips[numeric_cols])
print("\nStandardized Data:")
print(tips_standardized.head())



tips = sns.load_dataset('tips')
numeric_cols = tips.select_dtypes(include=['float64', 'int64'])
scaler = StandardScaler()
tips_standardized = tips.copy()

scaler=StandardScaler()
scaled_data=scaler.fit_transform(numeric_cols)

pca=PCA(n_components=2)
pca_result=pca.fit_transform(scaled_data)
pca_df=pd.DataFrame(data=pca_result,columns=['PC1','PC2'])
print(pca_df.head())


plt.scatter(pca_df['PC1'],pca_df['PC2'],alph=0.7)
plt.xlabel('Princial component 1')
plt.ylabel('Princial component 2')
plt.title('PCA Projection of tips dataset')
plt.show()

