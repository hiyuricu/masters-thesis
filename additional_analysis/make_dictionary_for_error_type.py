#!/usr/bin/python
# -*- coding: utf-8 -*-

# 挿入、削除、置換、転置といった誤りの割合を出力します
# sys.argv[1]はadditonal_analysis_corrected_error.txtやadditonal_analysis_un_corrected_error.txtです

import sys
from collections import defaultdict

def make_dictionary_for_error_type():

    dic_of = defaultdict(int)

    for line in open(sys.argv[1]):
      line = line.strip()
      word_list = line.split()
      dic_of[word_list[5]] += 1

    print dic_of

if __name__ == "__main__":
  make_dictionary_for_error_type()
