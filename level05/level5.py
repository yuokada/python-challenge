#!/usr/bin/python2.6

import pickle


def main():
    """docstring for main"""
    pic = pickle.load(open("banner.p"))
    for tup in pic:
        print("".join([s[0] * s[1] for s in tup]))


if __name__ == '__main__':
    ans = main()
    print("level 5's answer: ", end=' ')
    print(ans)
