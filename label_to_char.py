 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:11:13 2018

@author: wyt
"""
#直接根据已有的label_freechars.csv去生成freechars_update.csv

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


import os
import csv
import pandas as pd



def chars_update(label_file):
#    parent_dir = os.getcwd()#返回当前路径
#    label_path = os.path.join(parent_dir, label_file + '.csv')
    dic1 = {}
    for line in open(label_file).readlines()[1:]:#从第一行开始读，略过表头
        for char in line.split(',')[1].strip():
            if char not in dic1.keys():
                dic1[char] = 1
            else:
                dic1[char] += 1

#    char_path = os.path.join(parent_dir , 'chars_freechars.csv')
#    dic2 = {}
#    for line in open(char_path).readlines()[1:]:
#        for char in line.split(',')[1].strip():
#            if char not in dic2.keys():
#                dic2[char] = 1
#            else:
#                dic2[char] += 1
#
#    dic2.update(dic1)
    with open(os.path.join('/Users/wyt/Documents/', 'freechars_update.csv'), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['char', 'freq'])
        #f.write('char' + ',' + 'freq' + '\n')#注释掉的这两行的方式也可以
        for key, value in dic1.items():
#            f.write(key + ',' + str(value) + '\n')
            writer.writerow([key,str(value)])


if __name__ == '__main__':
   # args = parse_args()
   # chars_update(args.label_file)
    chars_update('/Users/wyt/Documents/label_freechars.csv')#下面这两行纯粹是练手的，只是为了试验一下
    data=pd.read_csv('/Users/wyt/Documents/freechars_update.csv')#,header=0,names=['char','fre'])#.drop_duplicates()
    data.rename(columns={'char':'image','freq':'fre'},inplace=True)#True代表在原来的基础上修改
