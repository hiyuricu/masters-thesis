#!/usr/bin/python
# -*- coding: utf-8 -*-

# 語末のスペリング誤りの割合を求めるスクリプトです
# インプットは error_frequency_dic.txt です
# アウトプットとしてを出力します

import sys
from collections import defaultdict

if __name__ == "__main__":
	error_all_freq = 0
	error_freq = 0
	for line in open(sys.argv[1]):
		if line != '\n':
			error_list = line.strip().split()
			if len(error_list[0]) == 7 and error_list[0][1:4] == "→":
				# print error_list[0]
				# error_all_freq += int(error_list[1])
				# if error_list[0][0] == error_list[0][4]:
				# 	print error_list[0][0], error_list[0][4],error_list[1]
				error_freq += int(error_list[1])

	print float(error_freq) * 100 / 859
	print error_freq
