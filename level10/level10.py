#!/usr/bin/python2.6
# -*-  coding:utf-8 -*-

import re

def main():
    """"""
    a = [1,11,21,1211,111221,]
    target = "1"
    max_time =  31
    for i in range(max_time):
        target =  count_converter(target)
        print target

def count_converter(number):
    number = str(number)
    result  = []
    pre_chr = number[0]
    counter = 0
    for i in range( len(number) ):
        if i == len(number)-1: # slow
            if pre_chr == number[i]:
                result.append((pre_chr, counter))
            else:
                result.append([pre_chr, counter])
                result.append([number[i], 1])
        else:
            if pre_chr == number[i]:
                counter += 1
            else:
                result.append((pre_chr, counter))
                counter = 1
                pre_chr = number[i]
    #print  result
    return  "".join([str(y)+str(x) for x,y in result])


if __name__ == '__main__':
    main()      
    count_converter(1)
    ### get  tuple  ->  create string.
    ### (n, len)    ->  "n"*len
