#!/usr/bin/python
# -*- coding: utf-8 -*-

# string_error_result.txtのタイプミスを統計的にまとめるスクリプトです
# インプットとしてstring_error_result.txtとします
# アウトプットとしてを出力します

import sys
from collections import defaultdict


def make_position_list():
	count_of_position_dic = defaultdict(int)
	for line in open(sys.argv[1]):
		error_string_list = line.strip().split()
		count_of_position_dic[error_string_list[7]] += 1
		count_of_position_dic[error_string_list[6] + ":" + error_string_list[7]] += 1

	return count_of_position_dic

if __name__ == "__main__":
	for k,v in sorted(make_position_list().items(), key=lambda x:x[1], reverse=True):
		if len(k) == 3:
			print k,float(v) / make_position_list()[k.split(":")[1]]
		elif len(k) == 1 or len(k) == 2:
			print k,v