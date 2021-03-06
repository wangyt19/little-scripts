import pandas as pd
import numpy as np
df1=pd.read_csv('./ccc/a.csv',dtype={'prediction':np.object})
df1.rename(columns={'image':'image','prediction':'收款人账号'},inplace=True)#true代表在原来的基础上修改
df2=pd.read_csv('./ccc/b.csv',dtype={'prediction':np.object})
df2.rename(columns={'image':'image','prediction':'收款人名称'},inplace=True)
df3=pd.read_csv('./ccc/c.csv',dtype={'prediction':np.float})
df3['prediction']=df3['prediction'].map(lambda x: x/100)
df3.rename(columns={'image':'image','prediction':'小写金额'},inplace=True)

df=pd.merge(df1,df2,df3,on=[image])

df.to_csv('./ccc/test.csv',header=True,index=False,float_format='%.2f')
