# Kevin Pietrow
# Regex searching on large text file

import re
import sys

# set up 2D list
allSearchResults = [None] * 20
for i in range(1):
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
    global totalSearches
    global allSearchResults
    
    # ask if user wants 'raw' mode for regular expressions
    userParams.append((raw_input("Would you like to add 'r' in front of the expression? (y/n): ")).lower())
    # ask user for regular expression to be searched
    userParams.append(raw_input("Please enter the Regular Expression to be searched (outside quotation marks will be added automatically): "))
    totalSearches += 1

    # perform regex search
    if userParams[0] == "y":
        foundRegex = re.findall('r'+userParams[1], textFile)
    elif userParams[0] == "n":
        foundRegex = re.findall(userParams[1], textFile)
    else:
        foundRegex = re.findall(userParams[1], textFile)

    if foundRegex != None:
        print foundRegex

        # store result and search parameters in global 2D list
        if totalSearches == 1:
            allSearchResults[0] = [foundRegex, userParams[0], userParams[1], totalSearches]
            print "Result has been stored. Its search number is 1."
        elif totalSearches == 21:
            print "I am sorry, but you have too many saved results to store another value."
        else:
            allSearchResults[totalSearches - 1] = [foundRegex, userParams[0], userParams[1], totalSearches]
            print "Result has been stored. Its search number is" + str(totalSearches)

    else:
        print "Search did not have any results."
    
    return

# One of the menu options. Will handle both querying user and searching for regex



def main_menu(textFile):
    """Main menu selection for user options in the script"""
    xFactor = True
    
    while xFactor:
        print ""
        print "1- Enter new search string"
        print "2- Access prior search result"
        print "3- Exit program"
        userInstr = raw_input("Selection: ")
        
        # call different functions depending on user input
        if userInstr == "1":
            print ""
            new_search_regex(textFile)
        elif userInstr == "2":
            print ""
            search_past_result()
        elif userInstr == "3":
            print "Exiting program now."
            sys.exit(0)
        else:
            print "Not a valid response, please try again."
            print ""
            continue
    

# This will be the central hub for the program.
# Will control when user decides to exit the program.





def search_past_result():
    """Search for prior result"""
    global allSearchResults
    
    searchNumber = raw_input("What was the search number of the result that you are interested in?: ")
    allSearchResults[int(searchNumber) - 1]
    return

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
