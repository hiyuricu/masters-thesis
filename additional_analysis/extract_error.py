#!/usr/bin/python
# -*- coding: utf-8 -*-

# 文字単位のミスを抽出するスクリプトです。
# インプットとしてcorrected_error_list.txtやun_corrected_error_list.txtを入力します。
# アウトプットとしてadditonal_analysis_corrected_error.txtとadditonal_analysis_un_corrected_error.txtを出力し、9つの項目はそれぞれ
# 編集前単語、編集後単語、編集距離、タイピング速度、ユーザ名、誤り分類、error_string、related_string、誤りの位置
# を表している。

# 文字を削除する場合(damerau_distance_type == "del"の場合)は削除する文字をerror_string、削除する文字の一つ前の文字をrelated_stringとする。
# delの場合は削除する文字の前後をrelated_stringとした方が適切っぽい。

# 文字を挿入する場合(damerau_distance_type == "ins"の場合)は挿入する文字の一つ後の文字(飛ばした文字の代わりに入力した文字)をerror_string、挿入する文字をrelated_stringとする。
# 文字を置換する場合(damerau_distance_type == "sub"の場合)は置換される文字をerror_string、置換する文字をrelated_stringとする。

# insertion, deletion, substitution, transposition
# ins, del, sub, tra

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
		# print line

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
						# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

					if typing_list[0][i + 1] != typing_list[1][i] and error_number == 2:
						error_position = str(i + 2)
						error_string = typing_list[0][i + 1]
						related_string = typing_list[1][i - 1]
						# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
						break

					if i == len(typing_list[1]) - 1:
						if error_number == 1:
							error_position = str(i + 2)
							error_string = typing_list[0][i + 1]
							related_string = typing_list[1][i]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

						error_position = str(i + 3)
						error_string = typing_list[0][i + 2]
						related_string = typing_list[1][i]
						# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

			elif len(typing_list[0]) - len(typing_list[1]) == -2:
				damerau_distance_type = "ins"
				error_number = 1
				for i in range(len(typing_list[0])):
					if typing_list[0][i] != typing_list[1][i] and error_number == 1:
						error_number += 1
						error_position = str(i + 1)
						error_string = typing_list[0][i]
						related_string = typing_list[1][i]
						# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

					if typing_list[0][i] != typing_list[1][i + 1] and error_number == 2:
						error_position = str(i + 1)
						error_string = typing_list[0][i]
						related_string = typing_list[1][i + 1]
						# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
						break

					if i == len(typing_list[0]) - 1:
						if error_number == 1:
							error_position = str(i + 2)
							error_string = "_"
							related_string = typing_list[1][i + 1]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

						error_position = str(i + 3)
						error_string = "_"
						related_string = typing_list[1][i + 2]
						# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

			elif len(typing_list[0]) - len(typing_list[1]) == 0:
				tra_flag = 0
				sub_flag = 0
				ins_flag = 0
				del_flag = 0
				for i in range(len(typing_list[0])):
					if typing_list[0][i] != typing_list[1][i]:
						if  typing_list[0][i] == typing_list[1][i + 1] and typing_list[0][i + 1] == typing_list[1][i]:
							damerau_distance_type = "tra"
							error_position = str(i + 1)
							error_string = typing_list[0][i]
							related_string = typing_list[1][i]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
							tra_flag = 1
						break

				sub_count = 0
				for i in range(len(typing_list[0])):
					if typing_list[0][i] != typing_list[1][i]:
						sub_count += 1

				if tra_flag == 0 and sub_count == 2:
					sub_flag = 1
					damerau_distance_type = "sub"
					for i in range(len(typing_list[0])):
						if typing_list[0][i] != typing_list[1][i]:
							error_position = str(i + 1)
							error_string = typing_list[0][i]
							related_string = typing_list[1][i]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

				if tra_flag == 0 and sub_flag == 0:
					for i in range(len(typing_list[0])):
						if ins_flag == 0 and del_flag == 0 and typing_list[0][i] != typing_list[1][i]:
							if typing_list[0][i + 1] == typing_list[1][i]:
								del_flag = 1
								damerau_distance_type = "del"
								error_position = str(i + 1)
								error_string = typing_list[0][i]
								related_string = typing_list[1][i - 1]
								# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
							else:
								ins_flag = 1
								damerau_distance_type = "ins"
								error_position = str(i + 1)
								error_string = typing_list[0][i]
								related_string = typing_list[1][i]
								# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

						if del_flag == 1 and typing_list[0][i + 1] != typing_list[1][i]:
							damerau_distance_type = "ins"
							error_position = str(i + 1)
							error_string = typing_list[0][i + 1]
							related_string = typing_list[1][i]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
							break

						if ins_flag == 1 and typing_list[0][i] != typing_list[1][i + 1]:
							damerau_distance_type = "del"
							error_position = str(i + 1)
							error_string = typing_list[0][i]
							related_string = typing_list[1][i]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
							break

						if ins_flag == 1 and i == len(typing_list[0]) - 2:
							damerau_distance_type = "del"
							error_position = str(i + 2)
							error_string = typing_list[0][i + 1]
							related_string = typing_list[1][i + 1]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
							break

						if del_flag == 1 and i == len(typing_list[0]) - 2:
							damerau_distance_type = "ins"
							error_position = str(i + 2)
							error_string = "_"
							related_string = typing_list[1][i + 1]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
							break

			elif len(typing_list[0]) - len(typing_list[1]) == 1:
				del_flag = 0
				sub_flag = 0
				for i in range(len(typing_list[1])):
					if del_flag == 0 and sub_flag == 0 and typing_list[0][i] != typing_list[1][i]:
						if i == len(typing_list[1]) - 1 or typing_list[0][i + 1] != typing_list[1][i + 1] and typing_list[0][i + 1] != typing_list[1][i]:
							damerau_distance_type = "del"
							error_position = str(i + 1)
							error_string = typing_list[0][i]
							related_string = typing_list[1][i - 1]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

							damerau_distance_type = "sub"
							error_position = str(i + 1)
							error_string = typing_list[0][i + 1]
							related_string = typing_list[1][i]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
							break

						elif typing_list[0][i + 1] == typing_list[1][i]:
							del_flag = 1
							damerau_distance_type = "del"
							error_position = str(i + 1)
							error_string = typing_list[0][i]
							related_string = typing_list[1][i - 1]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
						else:
							sub_flag = 1
							damerau_distance_type = "sub"
							error_position = str(i + 1)
							error_string = typing_list[0][i]
							related_string = typing_list[1][i]
							# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

					elif del_flag == 1 and typing_list[0][i + 1] != typing_list[1][i]:
						damerau_distance_type = "sub"
						error_position = str(i + 2)
						error_string = typing_list[0][i + 1]
						related_string = typing_list[1][i]
						# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
						break
					elif sub_flag == 1 and typing_list[0][i] != typing_list[1][i]:
						damerau_distance_type = "del"
						error_position = str(i + 1)
						error_string = typing_list[0][i]
						related_string = typing_list[1][i - 1]
						# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
						break
					elif sub_flag == 1 and i == len(typing_list[1]) - 1:
						damerau_distance_type = "del"
						error_position = str(i + 1)
						error_string = typing_list[0][i + 1]
						related_string = typing_list[1][i]
						# print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
						break

			elif len(typing_list[0]) - len(typing_list[1]) == -1:
				ins_flag = 0
				sub_flag = 0
				for i in range(len(typing_list[0])):
					if ins_flag == 0 and sub_flag == 0 and typing_list[0][i] != typing_list[1][i]:
						if i == len(typing_list[0]) - 1 or typing_list[0][i + 1] != typing_list[1][i + 1] and typing_list[0][i] != typing_list[1][i + 1]:
							damerau_distance_type = "ins"
							error_position = str(i + 1)
							error_string = typing_list[1][i + 1]
							related_string = typing_list[1][i]
							print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

							damerau_distance_type = "sub"
							error_position = str(i + 2)
							error_string = typing_list[0][i]
							related_string = typing_list[1][i + 1]
							print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
							break

						elif typing_list[0][i] == typing_list[1][i + 1]:
							ins_flag = 1
							damerau_distance_type = "ins"
							error_position = str(i + 1)
							error_string = typing_list[0][i]
							related_string = typing_list[1][i]
							print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
						else:
							sub_flag = 1
							damerau_distance_type = "sub"
							error_position = str(i + 1)
							error_string = typing_list[0][i]
							related_string = typing_list[1][i]
							print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position

					elif ins_flag == 1 and typing_list[0][i] != typing_list[1][i + 1]:
						damerau_distance_type = "sub"
						error_position = str(i + 1)
						error_string = typing_list[0][i]
						related_string = typing_list[1][i + 1]
						print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
						break
					elif sub_flag == 1 and typing_list[0][i] != typing_list[1][i]:
						damerau_distance_type = "ins"
						error_position = str(i + 1)
						error_string = typing_list[0][i]
						related_string = typing_list[1][i]
						print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
						break
					elif sub_flag == 1 and i == len(typing_list[0]) - 1:
						damerau_distance_type = "ins"
						error_position = str(i + 2)
						error_string = "_"
						related_string = typing_list[1][i + 1]
						print typing_list[0], typing_list[1], typing_list[2], typing_list[3], typing_list[4], damerau_distance_type, error_string, related_string, error_position
						break


if __name__ == "__main__":
	pair_compare()