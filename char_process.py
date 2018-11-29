#label_to_char,直接根据已有的label.csv文件生成chars_update.csv，(并根据chars_freechars.csv进行更新),完整版
#执行方式：python char_process.py label

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:11:13 2018

@author: wyt
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os
import csv
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
    )

    parser.add_argument(
        'label_file',
        help='name of the label csv',
    )

    args = parser.parse_args()
    return args


def chars_update(label_file):
    parent_dir = os.getcwd()
    #label_path = os.path.join(parent_dir, label_file + '.csv')
    dic1 = {}
    '''
    data=pd.read_csv(label_path,header=0)
    data=data['value']
    for i in range(1, len(data)):
        for char in data.iloc[i].strip():
            if char not in dic1.keys():
                dic1[char] = 1
            else:
                dic1[char] += 1    
     '''

    for line in open(label_file).readlines()[1:]:#从第一行开始读，略过表头
        linesplit=line.split(',')
        lenth=len(linesplit)
        if lenth>2:
            if ',' not in dic1.keys():
                dic1[','] =0+lenth-2
            else:       
                dic1[',']+=lenth-2
        lines=''
        for i in range(1,lenth):
            lines+=linesplit[i]
        for char in lines.strip():#去除首尾空格，注意这种会缺少空格，不过正常来讲不应该有空格的
            if char not in dic1.keys():
                dic1[char] = 1
            else:
                dic1[char] += 1
        
    char_path = os.path.join(parent_dir , 'chars_freechars.csv')
    dic2 = {}
    for line in open(char_path).readlines()[1:]:#从第一行开始读，略过表头
        linesplit=line.split(',')
        if len(linesplit)>2:
            dic2[',']=linesplit[2].strip()
        else:
            dic2[linesplit[0].strip()]=linesplit[1].strip()#注意这种会缺少空格，不过正常来讲不应该有空格的
    dic2.update(dic1)
    with open(os.path.join(parent_dir, 'freechars_update_withfreechars.csv'), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['char', 'freq'])
 #       f.write('char' + ',' + 'freq' + '\n')#以这种方式写入的时候会有问题，读的时候要加df=pd.read_csv('path',quoting=csv.QUOTE_NONE,delimiter="\n")
        for key, value in dic2.items():
        #    f.write(key + ',' + str(value) + '\n')
             writer.writerow([key,str(value)])



if __name__ == '__main__':
    args = parse_args()
    chars_update(args.label_file)
