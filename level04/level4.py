#!/usr/bin/python2.6

import re
import urllib2


def main():
    """docstring for main"""
    next_number = "12345"
    # next_number = "52899" # 52899   -> 66831
    while(next_number.isdigit()):
        next_number = get_nothing_num(next_number)
        print "get_next:", next_number

    return next_number


def get_nothing_num(number):
    """docstring for get_nothing_num"""
    pat = re.compile("and the next nothing is ([0-9]+)")
    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    page = urllib2.urlopen(base_url % number)
    string = "".join(page.readlines())
    page.close()
    number = pat.findall(string)
    if number:  # findall or  another method
        return number[0]
    else:
        return string
    """
       please refactoring  try-catch-finally.
       catch :urllib2.URLError
    """


if __name__ == '__main__':
    ans = main()
    print "level 3's answer: ",
    print ans
