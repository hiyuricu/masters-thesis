#!/usr/bin/python
# -*- coding: utf-8 -*-

# 修正前文字列と修正後文字列のペアを取り出すためのスクリプトです。
# インプットとしてタイピングゲームver2におけるlogdata.txtを用います。
# アウトプットとしてcorrected_error_list.txtを出力し、修正前文字列と修正後文字列のペアを取り出します。

import sys

def levenshtein_distance(a, b):
    m = [ [0] * (len(b) + 1) for i in range(len(a) + 1) ]

    for i in xrange(len(a) + 1):
        m[i][0] = i

    for j in xrange(len(b) + 1):
        m[0][j] = j

    for i in xrange(1, len(a) + 1):
        for j in xrange(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                x = 0
            else:
                x = 1
            m[i][j] = min(m[i - 1][j] + 1, m[i][ j - 1] + 1, m[i - 1][j - 1] + x)

    return m[-1][-1]

def print_corrected_error_pair(before_B_string,corrected_string,typing_speed,user_name):
	pre_correction_string_candidate_list = []
	pre_correction_string_candidate = ""
	lowest_levenshtein_distance = 1000

	for i in corrected_string:
		pre_correction_string_candidate = pre_correction_string_candidate + i
		pre_correction_string_candidate_list.append(pre_correction_string_candidate)

	for candidate in pre_correction_string_candidate_list:
		candidate_levenshtein_distance = levenshtein_distance(before_B_string,candidate)
		if candidate_levenshtein_distance <= lowest_levenshtein_distance:
			# print before_B_string,candidate,candidate_levenshtein_distance
			lowest_levenshtein_distance = candidate_levenshtein_distance
			pre_correction_string_candidate = candidate
			# print pre_correction_string_candidate

	pre_correction_string = before_B_string + pre_correction_string_candidate_list[-1][len(pre_correction_string_candidate):]

	print before_B_string,pre_correction_string_candidate,lowest_levenshtein_distance,typing_speed,user_name,pre_correction_string,corrected_string

def pair_compare():
	for line in open(sys.argv[1]):
		string = ""
		head_B_flag = 0
		type_data_list = line.strip().split(",")
		for i in type_data_list[0]:
			if i != "B":
				string = string + i
				head_B_flag = 0
			elif i == "B" and head_B_flag == 0:
				if string != "":
					print_corrected_error_pair(string,type_data_list[1],type_data_list[3],type_data_list[4])
				string = string[:-1]
				head_B_flag = 1
			else:
				string = string[:-1]

if __name__ == "__main__":
	pair_compare()
