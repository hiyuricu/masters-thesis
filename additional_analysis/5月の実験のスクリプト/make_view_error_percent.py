#!/usr/bin/python
# -*- coding: utf-8 -*-

# 文字の視覚的混同のスペリング誤りの割合を求めるスクリプトです
# インプットは shikakutekikondou.txt、error_frequency_dic.txt です
# アウトプットとしてを出力します

import sys
from collections import defaultdict

shikiichi_dic = defaultdict(float)

def make_shikiichi_dic():
	for line in open(sys.argv[1]):
		if line != '\n':
			shikiichi_list = line.strip().split()
			if float(shikiichi_list[2]) >= 0.75:
				shikiichi_dic[shikiichi_list[1]] = float(shikiichi_list[2])

if __name__ == "__main__":
	error_all_freq = 0
	error_freq = 0
	make_shikiichi_dic()
	for line in open(sys.argv[2]):
		if line != '\n':
			error_list = line.strip().split()
			if len(error_list[0]) == 7:
				error_all_freq += int(error_list[1])
			if len(error_list[0]) == 5:
				error_all_freq += int(error_list[1])
				string_pair = error_list[0][0] + ":" + error_list[0][4]
				if string_pair in shikiichi_dic and error_list[0][1:4] == "↑":
					# print error_list[0]
					error_freq += int(error_list[1])

	print float(error_freq) * 100 / 859
	print error_freq
