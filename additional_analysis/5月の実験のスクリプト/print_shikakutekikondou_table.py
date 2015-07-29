#!/usr/bin/python
# -*- coding: utf-8 -*-

# 文字の視覚的混同の表を出力するスクリプトです
# インプットは shikakutekikondou.txtです

import sys
from collections import defaultdict

shikiichi_dic = defaultdict(float)

def make_shikiichi_dic():
	for line in open(sys.argv[1]):
		if line != '\n':
			shikiichi_list = line.strip().split()
			shikiichi_dic[shikiichi_list[1]] = float(shikiichi_list[2])

	return shikiichi_dic

if __name__ == "__main__":
	a = 0
	alphabetTable = [chr(i) for i in xrange(97, 123)]
	for k,v in sorted(make_shikiichi_dic().items(), key=lambda x:x[1], reverse=True):
		if k[0] == "o" and k[2] in alphabetTable and a < 8:
			a += 1
			print " & " + k[2] + " & " + str(v)