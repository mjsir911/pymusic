#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

__appname__     = ""
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "msirabel@gmail.com"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

def replace(shcript):
    midway = re.sub(".*bash.*\n", '', shcript)
    midway = re.sub('beep', '', midway)
    midway = re.sub('[ ]{1,}', '', midway)
#    print(midway)
    #exit()
    print('if' not in midway[0:3])
    if '-f' not in midway[0:3]:
        midway = re.sub('-f', ', f:', midway)
        midway = re.sub('-l', ', l:', midway)
        midway = re.sub('-D', ', D:', midway)
        templist = midway.splitlines()
        print(templist)
    else:
        midway = re.sub('-f', ' ', midway)
        midway = re.sub('-l', ' ', midway)
        midway = re.sub('-D', ' ', midway)

    midway = re.sub('-n', '\n', midway)
    midway = re.sub('\n,', '\n', midway)
    midway = re.sub(".*exit.*\n", '', midway)
    midway = re.sub('\n ', '\n', midway) # Get rid of spaces in front

    finale = re.sub("\n\n", '', midway)

    # Get rid of first newline if any #ugh
    if not finale.splitlines()[0]:
        superfinale = finale[1:]

    return superfinale


def main():
    bash_file = open(sys.argv[1], 'r')
    print(replace(bash_file.read()))


if __name__ == '__main__':
    main()
