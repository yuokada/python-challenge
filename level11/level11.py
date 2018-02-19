#!/usr/bin/python2.6
# -*-  coding:utf-8 -*-

import PIL.Image


def main():
    img = PIL.Image.open("cave.jpg")
    # print img.format
    # print img.mode
    half = [x / 2 for x in img.size]
    odd = even = PIL.Image.new(img.mode, half)

    for x in range(0, img.size[0], 2):
        for y in range(0, img.size[1] / 2):
            odd.putpixel((x / 2, y / 2), img.getpixel(tuple([x, y])))
    odd.show()
    for x in range(1, img.size[0], 2):
        for y in range(1, img.size[1] / 2):
            even.putpixel((x / 2, y / 2), img.getpixel(tuple([x, y])))
    even.show()  # answer is evil


if __name__ == '__main__':
    main()
