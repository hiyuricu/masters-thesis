#!/usr/bin/python
# -*- coding: utf-8 -*-

# スペリング誤りに対応するアルファベットの頻度の全パターンを示す表を出力するスクリプトです。表は3つ出力します。
# インプットは .txtです

import sys
from collections import defaultdict

dic_corresponding_to_misspelling = defaultdict(int)
after_dic_corresponding_to_misspelling = defaultdict(int)
before_dic_corresponding_to_misspelling = defaultdict(int)

def make_dic_corresponding_to_misspelling():
	for i in range(ord("a"),ord("z") + 1):
		dic_corresponding_to_misspelling[chr(i) + '_'] = 0
		after_dic_corresponding_to_misspelling[chr(i) + '_'] = 0
		before_dic_corresponding_to_misspelling[chr(i) + '_'] = 0
		for j in range(ord("a"),ord("z") + 1):
			dic_corresponding_to_misspelling[chr(i) + chr(j)] = 0
			after_dic_corresponding_to_misspelling[chr(i) + chr(j)] = 0
			before_dic_corresponding_to_misspelling[chr(i) + chr(j)] = 0

	for line in open(sys.argv[1]):
		if line != '\n':
			error_list = line.strip().split()
			if len(error_list[0]) == 7 and error_list[0][1:4] == "↑" and error_list[0][0] not in ["0","1","2","3","4","5","6","7","8","9"]:
				dic_corresponding_to_misspelling[error_list[0][0] + '_'] += int(error_list[1])
			elif len(error_list[0]) == 5 and error_list[0][1:4] == "↑" and error_list[0][0] not in ["0","1","2","3","4","5","6","7","8","9"]:
				dic_corresponding_to_misspelling[error_list[0][0] + error_list[0][4]] += int(error_list[1])
			elif len(error_list[0]) == 7 and error_list[0][1:4] == "→" and error_list[0][0] not in ["0","1","2","3","4","5","6","7","8","9"]:
				after_dic_corresponding_to_misspelling[error_list[0][0] + '_'] += int(error_list[1])
			elif len(error_list[0]) == 5 and error_list[0][1:4] == "→" and error_list[0][0] not in ["0","1","2","3","4","5","6","7","8","9"]:
				after_dic_corresponding_to_misspelling[error_list[0][0] + error_list[0][4]] += int(error_list[1])
			elif len(error_list[0]) == 7 and error_list[0][1:4] == "←" and error_list[0][0] not in ["0","1","2","3","4","5","6","7","8","9"]:
				before_dic_corresponding_to_misspelling[error_list[0][0] + '_'] += int(error_list[1])
			elif len(error_list[0]) == 5 and error_list[0][1:4] == "←" and error_list[0][0] not in ["0","1","2","3","4","5","6","7","8","9"]:
				before_dic_corresponding_to_misspelling[error_list[0][0] + error_list[0][4]] += int(error_list[1])


if __name__ == "__main__":
	make_dic_corresponding_to_misspelling()


	print "入力すべき文字の頻度を示した表"
	print '誤り',"&",'\\_',"&",
	for i in range(ord("a"),ord("z") + 1):
		if chr(i) == 'z':
			print chr(i),"¥¥ ¥hline"
		else:
			print chr(i),"&",
	for k,v in sorted(dic_corresponding_to_misspelling.items()):
		if k[1] == 'z':
			print str(v),"¥¥ ¥hline"
		elif k[1] == '_':
			print k[0],"&",str(v),"&",
		else:
			print str(v),"&",

	print "\n1つ前の文字の頻度を示した表"

	print '誤り',"&",'\\_',"&",
	for i in range(ord("a"),ord("z") + 1):
		if chr(i) == 'z':
			print chr(i),"¥¥ ¥hline"
		else:
			print chr(i),"&",
	for k,v in sorted(after_dic_corresponding_to_misspelling.items()):
		if k[1] == 'z':
			print str(v),"¥¥ ¥hline"
		elif k[1] == '_':
			print k[0],"&",str(v),"&",
		else:
			print str(v),"&",

	print "\n1つ後の文字の頻度を示した表"

	print '誤り',"&",'\\_',"&",
	for i in range(ord("a"),ord("z") + 1):
		if chr(i) == 'z':
			print chr(i),"¥¥ ¥hline"
		else:
			print chr(i),"&",
	for k,v in sorted(before_dic_corresponding_to_misspelling.items()):
		if k[1] == 'z':
			print str(v),"¥¥ ¥hline"
		elif k[1] == '_':
			print k[0],"&",str(v),"&",
		else:
			print str(v),"&",

	print ""
