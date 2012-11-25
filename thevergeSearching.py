# Kevin Pietrow
# Regex searching on large text file

import re
import sys

allSearches = []
totalSearch = 0

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
    totalSearch += 1
    return re.findall(searchText, text)

def query_user():
    """Find user's search parameters"""
    userParams = []
    # ask if user wants 'raw' mode for regular expressions
    userParams.append((raw_input("Would you like to add 'r' in front of the expression? (y/n): ")).lower())
    # ask user for regular expression to be searched
    userParams.append(raw_input("Please enter the Regular Expression to be searched (outside quotation marks will be added automatically): "))
    searchInformation = regex_search(userParams)
    return searchInformation

def regex_search(information):
    """Perform a regex search on the text file"""

def main_menu():
    """Main menu selection for user options in the script"""
    xFactor = True
    while xFactor:
        print "1- Enter new search string"
        print "2- Access prior search result"
        print "3- Exit program"
        userInstr = raw_input("Selection: ")
        
        # call different functions depending on user input
        if userInstr == "1":
            inputInfo = query_user()
        elif userInstr == "2":
            inputInfo = search_result()
        elif userInstr == "3":
            print "Exiting program now."
            sys.exit(0)
        else:
            print "Not a valid response, please try again."
            continue
        
        # return list object with necessary information
        return inputInfo

def search_result():
    """Search for prior result"""
    searchNumber = raw_input("What was the search number of the result that you are interested in?: ")
    return allSearches[searchNumber - 1]
    

def main():
    xFactor = True
    # Print initial greeting
    print "Hello, and welcome to 'Searching TheVerge!'. Please select a menu option."
    # open file
    text = input_file('/Users/User/Documents/Python 2.7.3/Regex/TheVerge.txt')
    while xFactor:
        # get user's search parameters
        userInput = main_menu()

        # perform regex search based on user's specifications
        if userInput[0] == "y":
            output = search_file(userInput[1], "r"+text)
        elif userInput[0] == "n":
            output = search_file(userInput[1], text)
            
        print output
        userContinue = (raw_input("Would you like to input another search string? (y/n): ")).lower()
        if userContinue == "n":
            return
    return

main()
