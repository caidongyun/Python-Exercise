#!/usr/bin/python
# -*- coding: utf-8 -*-
# by JeffMa at http://devework.com/
"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
"""
filtered_file = open("filtered_words.txt")
filtered_word = filtered_file.read().split()
inputed_words = raw_input(u"请输入相关内容,按回车键结束:".encode("utf-8"))
inputed_words_array = inputed_words.split()
for word in filtered_word:
    if inputed_words.find(word) == 0:
        print "根据相关法律法规,已被和谐"
        quit()

print inputed_words