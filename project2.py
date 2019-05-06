import numpy as np
import pandas as pd
s=pd.Series([1,3.0,np.nan,15,7,8])#nan bydefault nature float
print(s)
dates=pd.date_range('20180101',periods=6,freq='D')#d refer as day and it can also be Y and M
print(dates[0])
print(np.random.randn(6,4))#6,4 matrix generate
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])
print(df)
print("Headings in Dataframe:",df.columns)
print("Row Headings in Dataframe:",df.index)
print("Values in Dataframe",df.values)
print(df.dtypes)
print(df.head(3))
print(df.tail(3))
print(df.sample(3))
print(df.describe(include='all'))
print(df.T)
print("original values:\n",df)
print("sorted values:\n",df.sort_values(by='B',ascending=True))
print("original values:\n",df)
print(df.A)
print(df['A'])
print(df[0:3])
#print("\n\n")
print(df.A> 0)

print(df[df.A> 0])
