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

def search_file(searchText, text):
    """Performs RegEx() with user's input"""
    return re.findall(searchText, text)

        

def main():
    # open file
    text = input_file('/Users/User/Documents/Python 2.7.3/Regex/TheVerge.txt')
    userInput = raw_input("What Regular Expression do you want searched? Please\n enter any and all parameters:")
    output = search_file(userInput, text)
    print output
    return

main()
