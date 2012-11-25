# Kevin Pietrow
# Regex searching on large text file

import re
import sys

# set up 2D list
allSearchResults = [None] * 1
for i in range(3):
    allSearchResults[i] = [None] * 4

# set up global counter for amount of searches
totalSearches = 0

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

# Necessary code

def new_search_regex(textFile):
    """Finds users search parameters, then performs RegEx() with user's input"""
    userParams = []
    # ask if user wants 'raw' mode for regular expressions
    userParams.append((raw_input("Would you like to add 'r' in front of the expression? (y/n): ")).lower())
    # ask user for regular expression to be searched
    userParams.append(raw_input("Please enter the Regular Expression to be searched (outside quotation marks will be added automatically): "))
    totalSearches += 1

    # perform regex search
    if userParams[0] == "y":
        foundRegex = re.findall('r'+userParams[1], text)
    if userParams[0] == "n":
        foundRegex = re.findall('r'+userParams[1], text)
        
    print foundRegex

    # store result and search parameters in global 2D list
    if totalSearches == 1:
        allSearchResults[0] = [foundRegex, userParams[0], userParams[1], totalSearches]
    else:
        allSearchResults[totalSearches - 1] = [foundRegex, userParams[0], userParams[1], totalSearches]

    return

# Necessary, but need to decide where it will be incorporated.


# Correct that this code is standalone, but need to decide if the regex should just be
# searched from within here.
#
# Also, I feel like there need to be more questions to the user, but can't think of them
# at this time.



def main_menu(textFile):
    """Main menu selection for user options in the script"""
    xFactor = True
    while xFactor:
        print "1- Enter new search string"
        print "2- Access prior search result"
        print "3- Exit program"
        userInstr = raw_input("Selection: ")
        
        # call different functions depending on user input
        if userInstr == "1":
            new_search_regex(textFile)
        elif userInstr == "2":
            search_result()
        elif userInstr == "3":
            print "Exiting program now."
            sys.exit(0)
        else:
            print "Not a valid response, please try again."
            continue
        
        # return list object with necessary information
        return

# Need to decide if this will be the central hub for the program, or the main() function
# As of now, the code has multiple different return values from functions all funneling
# through this one function





def search_result():
    """Search for prior result"""
    searchNumber = raw_input("What was the search number of the result that you are interested in?: ")
    return allSearchResults[searchNumber - 1]

# This function is necessary. Need to decide how it returns the searched for result,
# and need to build error checking into the search
    

def main():
    xFactor = True
    # Print initial greeting
    print "Hello, and welcome to 'Searching TheVerge!'. Please select a menu option."
    # open file
    text = input_file('/Users/User/Documents/Python 2.7.3/Regex/TheVerge.txt')
    while xFactor:
        # get user's search parameters
        main_menu(text)
    return

# Bit of a confusing mess at the moment. Need to simplify this function, and decide where
# the functionality contained here should go.

main()



# Ultimately, need to work out return sequence for values, which functions are necessary,
# and simplify the code where I can.
