#!/usr/bin/python
# -*- coding: utf-8 -*-

# 文字のキー配置によるスペリング誤りの割合を求めるスクリプトです
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
			if len(error_list[0]) == 7:
				error_all_freq += int(error_list[1])
			if len(error_list[0]) == 5 and error_list[0][1:4] == "↑":
				error_all_freq += int(error_list[1])
				if error_list[0][0] == "a" and error_list[0][4] in ["q","s","z"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "q" and error_list[0][4] in ["a","w"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "z" and error_list[0][4] in ["a","x"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "l" and error_list[0][4] in ["k","p"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "p" and error_list[0][4] in ["o","l"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "m" and error_list[0][4] in ["k","n"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "w" and error_list[0][4] in ["q","a","s","e"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "e" and error_list[0][4] in ["w","d","s","r"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "r" and error_list[0][4] in ["e","d","f","t"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "t" and error_list[0][4] in ["r","f","g","y"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "y" and error_list[0][4] in ["t","g","h","u"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "u" and error_list[0][4] in ["y","h","j","i"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "i" and error_list[0][4] in ["u","j","k","o"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "o" and error_list[0][4] in ["i","k","l","p"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "x" and error_list[0][4] in ["z","s","d","c"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "c" and error_list[0][4] in ["x","d","f","v"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "v" and error_list[0][4] in ["c","f","g","b"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "b" and error_list[0][4] in ["v","g","h","n"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "n" and error_list[0][4] in ["b","h","j","m"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "s" and error_list[0][4] in ["a","w","e","d","z","x"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "d" and error_list[0][4] in ["s","e","r","f","c","x"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "f" and error_list[0][4] in ["d","r","t","g","v","c"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "g" and error_list[0][4] in ["f","t","y","h","b","v"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "h" and error_list[0][4] in ["g","y","u","j","n","b"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "j" and error_list[0][4] in ["h","u","i","k","m","n"]:
					error_freq += int(error_list[1])
				elif error_list[0][0] == "k" and error_list[0][4] in ["j","i","o","l","m"]:
					error_freq += int(error_list[1])

	print float(error_freq) * 100 / (859 * 1)
