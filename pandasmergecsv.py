import pandas as pd
import numpy as np
df1=pd.read_csv('./ccc/a.csv')
df1.rename(colums={'image':'image','prediction':'收款人账号'},inplace=True)#true代表在原来的基础上修改
df2=pd.read_csv('./ccc/b.csv')
df2.rename(colums={'image':'image','prediction':'收款人名称'},inplace=True)
df=pd.merge(df1,df2,on=[image])

df.to_csv('./ccc/test.csv',header=True,index=False,float_format='%.2f')
