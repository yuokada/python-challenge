#!/usr/bin/python2.6

import re
import urllib2

def main():
    """docstring for main"""
    next_number = 12345
    next_number = 34684 # shorter
    while(next_number > 0):
        print next_number
        tmp = get_nothing_num(next_number)
        print  "get_next" , tmp
        next_number = tmp
    print  next_number

def get_nothing_num(number):
    """docstring for get_nothing_num"""
    pat      = re.compile("and the next nothing is ([0-9]+)")
    base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
    page     = urllib2.urlopen(base_url % number)
    number   = pat.findall("".join(page.readlines()))[0] # findall or  another method
    page.close()
    return number
    """
       please refactoring  try-catch-finally.
    """

if __name__ == '__main__':
    ans = main()
    print "level 3's answer: ", 
    print  ans
