#!/usr/bin/python2.6

import PIL.Image

def main():
    img = PIL.Image.open("./wire.png")
    ans = PIL.Image.new(img.mode,  (100,100))


    # x 0 -> 100 ->0 -> 99
    # (0,0) -> (100,0) -> (100,100) -> (0,100) -> (0,1) -> (99,1)
    res  = [[0]*100 for i in range(100)] # nul list
    xmax = ymax = 100
    xmin = ymin = 0
    x    = y    = 0
    for i  in range(1, 10000):
        if x == y   :
            res[x][y] = i
            x += 1
        else:
            pass
    for n in range(1,10,1):
       matrix(n)

    return
#    ls  = list(img.getdata())
#    ls.reverse()
#    sa  = []
#    for i in range(10000):
#        sa.append(img.getpixel( tuple([i,0]) ) )

def matrix(square=None):
    if square > 1:
        res  = [[0]*square for i in range(square)] # nul list
        
        # set start  position
        x = 0
        y = 0
        if square % 2 :
            x = (square + 1)/2 -1 
            y = (square + 1)/2 -1
            res[x][y] = 1
        else:
            x = (square)/2 + 1 -1 
            y = (square)/2 - 1 
            res[x][y]    = 1

        posisions  = [n for n in range(0,square**2)]
        # pick  around
        mode = 0
        for n in posisions:
            if   mode == 0:
                x += 1 
                pass
            elif mode == 1:
                pass
            elif mode == 2:
                pass
            elif mode == 3:
                pass
            else:
                print "what happed?"

        print res
    else:
        print "fuck you"

if __name__ == '__main__':
    # jyoutai-hennsuu 4
    # ulam's spiral 
    main()  
