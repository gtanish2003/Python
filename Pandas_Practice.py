import pandas as pd

print(pd.__version__)

A=pd.Series([2,3,4,5],index=['a','b','c','d'])
#print(A)
#print(A.values)
#print(A.index)

B=pd.Series([10,20,30,40],index=['a','b','c','d'])
df=pd.DataFrame({'Marks':A,'Marks Expected':B})
print(df)

print(A.loc['a':'c'])
print(A.iloc[1:3])


