
#直接根据已有的label_freechars.csv去生成freechars_update_withoutfreechars.csv

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
import numpy as np


def chars_update(label_file):
#    parent_dir = os.getcwd()#返回当前路径
#    label_path = os.path.join(parent_dir, label_file + '.csv')
    dic1={}
    for line in open(label_file).readlines()[1:]:#从第一行开始读，略过表头
        linesplit=line.split(',')
        lenth=len(linesplit)
        if lenth>2:
            if ',' not in dic1.keys():
                dic1[',']=0+lenth-2
            else:
                dic1[',']+=lenth-2
        lines=''
        for i in range(1,lenth):
            lines+=linesplit[i]
        for char in lines.strip():#去除首尾空格,注意这种会缺少空格，不过正常来讲不应该有空格的
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
    with open(os.path.join('/home/wangyinting/icbc_ocr_deploy/recognition', 'freechars_update_withoutfreechars.csv'), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['char', 'freq'])
        #f.write('char' + ',' + 'freq' + '\n')#注释掉的这两行的方式也可以,但是以pandas读入这种方式生成的csv时会有问题，不建议以这种方式写,读的时候要加df=pd.read_csv('path',quoting=csv.QUOTE_NONE,delimiter="\n")
        for key, value in dic1.items():
#            f.write(key + ',' + str(value) + '\n')#这两种方式要分别配套使用，不可混用
            writer.writerow([key,str(value)])


if __name__ == '__main__':
   # args = parse_args()
   # chars_update(args.label_file)
    chars_update('/home/wangyinting/icbc_ocr_deploy/recognition/label_freechars.csv')


