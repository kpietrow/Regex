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

def query_user():
    """Find user's search parameters"""
    userParams = []
    # ask if user wants 'raw' mode for regular expressions
    userParams.append((raw_input("Would you like to add 'r' in front of the expression? (y/n):")).lower())
    # ask user for regular expression to be searched
    userParams.append(raw_input("Please enter the Regular Expression to be searched (outside quotation marks will be added automatically):"))
    return userParams                     
    

        

def main():
    xFactor = True
    allSearches = []
    # open file
    text = input_file('/Users/User/Documents/Python 2.7.3/Regex/TheVerge.txt')
    while xFactor:
        # get user's search parameters
        userInput = query_user()

        # perform regex search based on user's specifications
        if userInput[0] == "y":
            output = search_file(userInput[1], "r"+text)
        elif userInput[0] == "n":
            output = search_file(userInput[1], text)
            
        print output
        userContinue = (raw_input("Would you like to input another search string? (y/n):")).lower()
        if userContinue == "n":
            return
    return

main()
