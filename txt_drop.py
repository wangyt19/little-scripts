#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:07:34 2018

@author: wyt
"""

import pandas as pd
import numpy as np


txtfile='/Users/wyt/Downloads/代码deeptext等/大藏经分类/5000/data_5k/testtxt.txt'
data=pd.read_csv(txtfile,sep=" ",header=None,names=['date','1','2','3','4','5'])#.drop_duplicates()
l0 = len(data)
print(data,'orlen')
data1=data.drop_duplicates(subset = 'date')#如果不写subset的话，就是两行所有的内容都相同才会删除一个，写了subset就是按照subset那一列来进行的去重
l1=len(data1)
print(data1,'lendropduplicate')
#data2 = pd.DataFrame(data['label'].unique())
#l2 = len(data2)
#print(l2,'lenunique')

txtfile1='/Users/wyt/Downloads/代码deeptext等/大藏经分类/5000/data_5k/synset.txt'
data2=pd.read_csv(txtfile1,sep=" ",header=None,names=['label','char'])#.drop_duplicates()
l2 = len(data2)
print(l2,data2,'orlen')
data3=data2.drop_duplicates(subset = 'char')
l3=len(data3)
print(l3,data3,'lendropduplicate')
#data2 = pd.DataFrame(data['label'].unique())
#l2 = len(data2)
#print(l2,'lenunique')
