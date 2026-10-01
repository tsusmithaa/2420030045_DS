import pandas as pd
data={'col1':[1,2,3,4],'col2':[10,20,30,40]}
pd.DataFrame.from_dict(data)

data={'row1':['s','q','e','b','d'],'row2':[10,20,30,40]}
pd.DataFrame.from_dict(data,orient='index',columns=['col1','col2','col3','col4','col5'])            

