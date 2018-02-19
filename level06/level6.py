#!/usr/bin/python2.6

import zipfile
import re


def main():
    """docstring for main"""
    zfh = zipfile.ZipFile("channel.zip")
    file_num = 90052  # Next nothing is 94191
    pat = re.compile("([0-9]+)")
    answer = []
    while file_num != 46145:
        str = zfh.read("%s.txt" % file_num)
        file_num = int(pat.findall(str)[0])
        answer.append(zfh.getinfo("%s.txt" % file_num).comment)

    zfh.close()
    return "".join(answer)


if __name__ == '__main__':
    ans = main()
    print("level 6's answer: ", end=' ')
    print(ans)
