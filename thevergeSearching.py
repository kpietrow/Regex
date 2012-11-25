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

# Necessary code

def search_file(searchText, text):
    """Performs RegEx() with user's input"""
    totalSearch += 1
    return re.findall(searchText, text)

# Necessary, but need to decide where it will be incorporated.

def query_user():
    """Find user's search parameters"""
    userParams = []
    # ask if user wants 'raw' mode for regular expressions
    userParams.append((raw_input("Would you like to add 'r' in front of the expression? (y/n): ")).lower())
    # ask user for regular expression to be searched
    userParams.append(raw_input("Please enter the Regular Expression to be searched (outside quotation marks will be added automatically): "))
    searchInformation = regex_search(userParams)
    
    return searchInformation

# Correct that this code is standalone, but need to decide if the regex should just be
# searched from within here.
#
# Also, I feel like there need to be more questions to the user, but can't think of them
# at this time.

def regex_search(information):
    """Perform a regex search on the text file"""
    
# Version of code already exists in search_file().
#
# Need to decide if this function will be standalone, part of query_user(), or part of
# main(). Could be good as standalone as error checking could be done here.
#
# If it is standalone though, need to fully figure out how new listing will be carried
# back to main(), or if it will be displayed here.

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

# Need to decide if this will be the central hub for the program, or the main() function
# As of now, the code has multiple different return values from functions all funneling
# through this one function





def search_result():
    """Search for prior result"""
    searchNumber = raw_input("What was the search number of the result that you are interested in?: ")
    return allSearches[searchNumber - 1]

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

# Bit of a confusing mess at the moment. Need to simplify this function, and decide where
# the functionality contained here should go.

main()



# Ultimately, need to work out return sequence for values, which functions are necessary,
# and simplify the code where I can.
