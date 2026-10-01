import pandas as pd 
import numpy as np
from scipy.spatial import distance
from scipy.stats import spearmanr

pointA= np.array([1, 2, 3])
pointB= np.array([4, 5, 6])

minkowski_distance_p3= distance.minkowski(pointA,pointB, p=3)
print("Minkowski distance with p3:", minkowski_distance_p3)
#similarity (inverse of distance)
similarity= 1/(1+minkowski_distance_p3)
print("Similarity:", similarity)

eclidean_distance= distance.euclidean(pointA,pointB)
print("Euclidean distance:", eclidean_distance) 
similarity_euclidean= 1/(1+eclidean_distance)
print("Similarity (Euclidean):", similarity_euclidean)

manhattan_distance= distance.cityblock(pointA,pointB)
print("Manhattan distance:", manhattan_distance)
similarity_manhattan= 1/(1+manhattan_distance)
print("Similarity (Manhattan):", similarity_manhattan)


df=pd.DataFrame({
    'X': [10, 20, 30, 40, 50],
    'Y': [15, 25, 35, 45, 55]   
})

corr_matrix= df.corr(method='pearson')
print("Correlation matrix:\n", corr_matrix)


 
dff=pd.DataFrame({
    'DS': [90, 80, 70, 60, 50],
    'CD': [50, 60, 70, 80, 90],
    'TOC': [80, 90, 40, 50, 60]
})

sub_corr_matrix= dff.corr(method='pearson')
print("Pearson correlation matrix:\n", sub_corr_matrix)
dff2=pd.read_csv("Iris.csv")
print(dff2.corr(method='pearson',numeric_only=float))

corr_value,p_value=spearmanr(df['X'], df['Y'])
print("Spearman correlation coefficient:", corr_value)
print("P-value:", p_value)


#subjective correlation
df_sub=pd.DataFrame({
    "DS": [90, 80, 70, 60, 50],
    "CD": [50, 60, 70, 80, 90],
    "TOC": [80, 90, 40, 50, 60]
})
corr_sub_value, p_value_sub= spearmanr(df_sub['DS'], df_sub['CD'])
print("Spearman correlation coefficient (subset):", corr_sub_value)
corr_sub_value, p_value_sub= spearmanr(df_sub['CD'], df_sub['TOC'])
print("Spearman correlation coefficient (subset):", corr_sub_value)
corr_sub_value, p_value_sub= spearmanr(df_sub['DS'], df_sub['TOC'])
print("Spearman correlation coefficient (subset):", corr_sub_value)

def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))


ham_dst=hamming_distance("susmitha is in cse", "manvitha is in cse")
print("Hamming distance:", ham_dst)

#lcs length
def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n ):
            if X[i]==Y[j]:
                dp[i][j]=dp[i][j]+1
            else:
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
    return dp[m][n]

seq1="susmitha"
seq2="susmitha"
length=lcs_length(seq1, seq2)
print("Length of Longest Common Subsequence:", length)
