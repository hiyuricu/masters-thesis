#!/usr/bin/python
# -*- coding: utf-8 -*-

# string_error_result.txtのタイプミスを統計的にまとめるスクリプトです
# インプットとしてstring_error_result.txtとします
# アウトプットとしてerror_frequency_dic.txtを出力します
# e,e←l,e↑i,e→e,

import sys
from collections import defaultdict


def make_error_list():
	count_of_error_dic = defaultdict(int)
	for line in open(sys.argv[1]):
		error_string_list = line.strip().split()
		# count_of_error_dic[error_string_list[0]] += 1
		# count_of_error_dic[error_string_list[0] + "←" + error_string_list[1]] += 1
		# count_of_error_dic[error_string_list[0] + "↑" + error_string_list[2]] += 1
		count_of_error_dic[error_string_list[0] + "→" + error_string_list[3]] += 1


	return count_of_error_dic

if __name__ == "__main__":
	for k,v in sorted(make_error_list().items(), key=lambda x:x[1], reverse=True):
		print k,v