#!/usr/bin/python2.6

import re

def main():
    """docstring for main"""
    f   = open("ocr.html")
    pat = re.compile("[a-z]")
    answer_list = []
    for line in f.readlines():
        if pat.search(line) :
            match =  pat.findall(line)
            print match 
            answer_list.extend(match)

    return  "".join(answer_list)

if __name__ == '__main__':
    ans = main()
    print "level 2's answer: ", 
    print  ans
