#!/usr/bin/python2.6

import re

def main():
    """docstring for main"""
    f   = open("equality.html")
    pat = re.compile("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]")
    answer_list = []
    for line in f.readlines():
        if pat.search(line) :
            match =  pat.findall(line)
            for string in match:
                answer_list.append(string[4])

    return  "".join(answer_list)

if __name__ == '__main__':
    ans = main()
    print "level 3's answer: ", 
    print  ans
