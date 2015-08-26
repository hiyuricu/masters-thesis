#!/usr/bin/python
# -*- coding: utf-8 -*-

# 修正されない誤りのペアを取り出すためのスクリプトです。
# インプットとしてタイピングゲームver2におけるlogdata.txtを用います。
# アウトプットとしてun_corrected_error_list.txtを出力します。

import sys

def levenshtein_distance(a, b):
    m = [ [0] * (len(b) + 1) for i in range(len(a) + 1) ]

    for i in xrange(len(a) + 1):
        m[i][0] = i

    for j in xrange(len(b) + 1):
        m[0][j] = j

    for i in xrange(1, len(a) + 1):
        for j in xrange(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                x = 0
            else:
                x = 1
            m[i][j] = min(m[i - 1][j] + 1, m[i][ j - 1] + 1, m[i - 1][j - 1] + x)

    return m[-1][-1]

def pair_compare():
	for line in open(sys.argv[1]):
		type_data_list = line.strip().split(",")
		if type_data_list[1] != type_data_list[2]:
			print type_data_list[1], type_data_list[2], levenshtein_distance(type_data_list[1], type_data_list[2]), type_data_list[3], type_data_list[4]

if __name__ == "__main__":
	pair_compare()
