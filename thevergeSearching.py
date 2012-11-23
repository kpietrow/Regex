# Kevin Pietrow
# Regex searching on large text file

import re
import sys

# open text file
def input_file(fileName):
    """Open file"""
    try:
        rt = open(fileName, 'r')
    except IOError:
        print "Failure to locate file. Program will exit."
        sys.exit(0)

    text = rt.read()
    return text

def main():
    # open file
    text = input_file('/Users/User/Documents/Python 2.7.3/Regex/LargeText.txt
