#!/usr/bin/python2.6

import re
import PIL.Image

def main():
    img = PIL.Image.open("oxygen.png")
    
    length_x,length_y = img.size      #(629,95)
    #print img.format    # PNG
    for x in range(0,length_x,7):
        for y in range(length_y):
            if y == length_y/2:
                r,g,b,a = img.getpixel((x,y))
                if  r == g == b :
                    #print x,y ,img.getpixel((x,y))
                    print chr(r),
    print 
    answers =[105,110,116,101,103,114,105,116,121]
    return "".join([ chr(s) for  s in answers])

if __name__ == '__main__':
    ans = main()
    print "level 6's answer: ", 
    print  ans
