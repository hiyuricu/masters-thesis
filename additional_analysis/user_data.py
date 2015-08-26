#!/usr/bin/python
# -*- coding: utf-8 -*-

# 各ユーザのタイピング速度と入力文字数を出力します(この順番で出力します)
# sys.argv[1]はlogdata.txtとします

import sys
from collections import defaultdict

def user_data():

	typespeed_dic = defaultdict(float)
	total_speed_dic = defaultdict(float)
	total_type_strings_dic = defaultdict(float)

	for line in open(sys.argv[1]):
		line = line.strip()
		logdata_list = line.split(",")

		total_speed_dic[logdata_list[4]] += int(logdata_list[3])
		total_type_strings_dic[logdata_list[4]] += len(logdata_list[1])

	for user, total_speed in sorted(total_speed_dic.items(), key=lambda x:x[0], reverse=False):
		typespeed_dic[user] = total_speed / total_type_strings_dic[user]
		print user, typespeed_dic[user]

	for user, type_strings in sorted(total_type_strings_dic.items(), key=lambda x:x[0], reverse=False):
		print user, type_strings


if __name__ == "__main__":
  user_data()