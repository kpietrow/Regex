# Kevin Pietrow
# For use of Regular Expressions

import re
import sys

def open_file(fileName):
    """Open text file to be used"""
    try:
        text = open(fileName, 'r')
    except IOError:
        print "Failure to locate file. Script will exit."
        sys.exit(0)

    textFile = text.read()
    return textFile

def main():
    # open file
    text = open_file('/Users/User/Documents/Python 2.7.3/Regex/words.txt')
    results = re.findall(r"[S]+[A-Z]+", text)
    print results
    return

main()
