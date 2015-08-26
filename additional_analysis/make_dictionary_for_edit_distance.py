#!/usr/bin/python
# -*- coding: utf-8 -*-

# 編集距離の割合を出力します
# sys.argv[1]はadditonal_analysis_corrected_error.txtやadditonal_analysis_un_corrected_error.txtです

import sys
from collections import defaultdict

def make_dictionary_for_edit_distance():

    dic_of = defaultdict(int)

    for line in open(sys.argv[1]):
      line = line.strip()
      word_list = line.split()
      dic_of[word_list[2]] += 1

    print dic_of

if __name__ == "__main__":
  make_dictionary_for_edit_distance()
