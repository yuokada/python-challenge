#!/usr/bin/python2.6
# -*-  coding:utf-8 -*-

import re

def main():
    a = ["1",]
    target = a[0]
    max_time =  33
    for i in range(max_time):
        target =  count_converter(target)
        a.append(target)

    for j in range(len(a)):
        print j, len(a[j]), a[j]

def count_converter(number):
    result  = []
    pre_chr = number[0]
    counter = 0
    for i in range( len(number) ):
        if i == (len(number)-1): # slow
            if pre_chr == number[i]:
                counter += 1
                result.append([pre_chr, counter])
            else:
                result.append([pre_chr, counter])
                result.append([number[i], 1])
        else:
            if pre_chr == number[i]:
                counter += 1
            else:
                result.append([pre_chr, counter])
                counter = 1
                pre_chr = number[i]
    return  "".join([str(y)+str(x) for x,y in result])

if __name__ == '__main__':
    main()      
