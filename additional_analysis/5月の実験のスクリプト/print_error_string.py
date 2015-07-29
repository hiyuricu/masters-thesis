#!/usr/bin/python
# -*- coding: utf-8 -*-

# 文字単位のミスを抽出するスクリプトです
# インプットとして5gatu_no_alltypo.txtとします
# アウトプットとして5gatu_no_alltypo.txtをだし、4つの項目があり、順番にタイプミスの文字、英単語の前の文字、英単語そのものの文字、英単語の後の文字、被験者が入力した文字列、文字列に対応した英単語、タイプミスした文字の位置、英単語の長さとなっている。
import sys

def pair_compare():
	for line in open(sys.argv[1]):
		# print line
		typing_list = line.strip().split(",")
		hikensha_string_list = list(typing_list[0])
		eitango_string_list = list(typing_list[1])
		for i in range(len(hikensha_string_list)):
			if hikensha_string_list[i] != eitango_string_list[i]:
				if i == 0:
					print hikensha_string_list[i],"xxx",eitango_string_list[i],eitango_string_list[i + 1],typing_list[0],typing_list[1],i + 1,len(eitango_string_list)
				elif i + 1 == len(eitango_string_list):
					print hikensha_string_list[i],eitango_string_list[i - 1],eitango_string_list[i],"xxx",typing_list[0],typing_list[1],i + 1,len(eitango_string_list)
				else:
					print hikensha_string_list[i],eitango_string_list[i - 1],eitango_string_list[i],eitango_string_list[i + 1],typing_list[0],typing_list[1],i + 1,len(eitango_string_list)
				break

if __name__ == "__main__":
	pair_compare()