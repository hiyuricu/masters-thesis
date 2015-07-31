#!/usr/bin/python
# -*- coding: utf-8 -*-

# 文字単位のミスを抽出するスクリプトです。
# インプットとしてcorrected_error_list.txtやun_corrected_error_list.txtを入力します。
# アウトプットとしてadditonal_analysis_error.txtを出力し、？つの項目はそれぞれ、を表している。

# 文字が削除する場合(damerau_distance_type == "del"の場合)は削除する文字をerror_string、削除する文字の一つ前の文字をrelated_stringとする。
# 文字が挿入する場合(damerau_distance_type == "ins"の場合)は挿入する文字の一つ後の文字をerror_string、挿入する文字をrelated_stringとする。
# 文字が置換する場合(damerau_distance_type == "sub"の場合)は置換される文字をerror_string、置換する文字をrelated_stringとする。


# insertion, deletion, substitution, transposition
import sys

def pair_compare():
	for line in open(sys.argv[1]):
		damerau_distance_type = ""
		error_string = ""
		related_string = ""
		error_position = ""
		line = line.strip()
		typing_list = line.split()

		# if int(typing_list[2]) >= 3:
		# 	print line

		if typing_list[2] == "1":
			if len(typing_list[0]) == len(typing_list[1]):
				damerau_distance_type = "sub"
			elif len(typing_list[0]) > len(typing_list[1]):
				damerau_distance_type = "del"
			else:
				damerau_distance_type = "ins"

			for i in range(len(typing_list[0])):
				if typing_list[0][i] != typing_list[1][i]:
					if damerau_distance_type == "sub":
						error_position = str(i + 1)
						error_string = typing_list[0][i]
						related_string = typing_list[1][i]
					elif damerau_distance_type == "del":
						error_position = str(i + 1)
						error_string = typing_list[0][i]
						related_string = typing_list[1][i - 1]
					elif damerau_distance_type == "ins":
						error_position = str(i + 1)
						error_string = typing_list[0][i]
						related_string = typing_list[1][i]
					# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
					break

				elif i == len(typing_list[0]) - 1: # len(typing_list[0]) < len(typing_list[1])で、挿入する文字の場所が単語の最後尾だった場合
					error_position = str(i + 2)
					error_string = "_" # 挿入する文字の場所が最後尾だった場合
					related_string = typing_list[1][i + 1]
					# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
					break
				elif i == len(typing_list[1]) - 1: # len(typing_list[0]) > len(typing_list[1])で、削除する文字の場所が単語の最後尾だった場合
					error_position = str(i + 2)
					error_string = typing_list[0][i + 1]
					related_string = typing_list[1][i]
					# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
					break

		elif typing_list[2] == "2":

			if len(typing_list[0]) - len(typing_list[1]) == 2:
				damerau_distance_type = "del"
				error_number = 1
				for i in range(len(typing_list[1])):
					if typing_list[0][i] != typing_list[1][i] and error_number == 1:
						error_number += 1
						error_position = str(i + 1)
						error_string = typing_list[0][i]
						related_string = typing_list[1][i - 1]
						print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

					if typing_list[0][i + 1] != typing_list[1][i] and error_number == 2:
						error_position = str(i + 2)
						error_string = typing_list[0][i + 1]
						related_string = typing_list[1][i - 1]
						print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
						break

					elif i == len(typing_list[1]) - 1:
						if error_number == 1:
							error_position = str(i + 2)
							error_string = typing_list[0][i + 1]
							related_string = typing_list[1][i]
							print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

						error_position = str(i + 3)
						error_string = typing_list[0][i + 2]
						related_string = typing_list[1][i]
						print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position































if __name__ == "__main__":
	pair_compare()