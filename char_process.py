from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import os
import csv


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
    label_path = os.path.join(parent_dir, label_file + '.csv')
    dic1 = {}
    for line in open(label_path).readlines()[1:]:
        for char in line.split(',')[1].strip():
            if char not in dic1.keys():
                dic1[char] = 1
            else:
                dic1[char] += 1

    char_path = os.path.join(parent_dir , 'chars_freechars.csv')
    dic2 = {}
    for line in open(char_path).readlines()[1:]:
        dic2[line.split(',')[0].strip()]=line.split(',')[1].strip()

    dic2.update(dic1)
    with open(os.path.join(parent_dir, 'chars_update.csv'), 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['char', 'freq'])
        for key, value in dic2.items():
            f.write(key + ',' + str(value) + '\n')


if __name__ == '__main__':
    args = parse_args()
    chars_update(args.label_file)
