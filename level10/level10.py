#!/usr/bin/python2.6
# -*-  coding:utf-8 -*-

import re

def main():
    a = ["1",]
    target = a[0]
    max_time =  33
    for i in range(max_time):
        target =  counter(target)
        a.append(target)

    for j in range(len(a)):
        print j, len(a[j]), a[j]

def counter(number):
    pat = re.compile("(\d)\\1*")
    result = []
    for num_str in pat.finditer( str(number) ):
        result.append(num_str.group(0))
    return "".join( str(len(elem)) + elem[0] for elem  in  result )

if __name__ == '__main__':
    main()      
