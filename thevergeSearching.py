# Kevin Pietrow
# Regex searching on large text file


# NOTE: Need to create a class for regex() search results. This 2D
# Array approach has limited capacity, and is not OOP centric.
# Objects are a better approach and should be implemented as
# soon as possible. Even if the search and get result functions
# are not a part of the class, the results should still be
# stored as objects.



import re
import sys
import os

# set up 2D list
"""
allSearchResults = [None] * 50
for i in range(1):
    allSearchResults[i] = [None] * 4
"""

# Class for searches
class Reg_Search(object):

    def __init__(self, expression, result, search_number):
        self.expression = expression
        self.result = result
        self.search_number = search_number

    def display_search(self):
        print "Search number: " + self.search_number + "\n\nExpression searched: " + self.expression +
        "\n\nResult: " + self.result

# set up global counter for amount of searches
totalSearches = 0


def input_file():
    """Open file"""
    textFile = raw_input("What file would you like to search?: ")
    while True:
        try:
            rt = open(os.path.abspath(textFile), 'r')
        except IOError:
            print "Failure to locate file."
            textFile = raw_input("Please enter a different file: ")
            continue
        else:
            break

    text = rt.read()
    return text

# Necessary code. This opens up the text file that the user requested.


def new_search_regex(textFile):
    """Finds users search parameters, then performs RegEx() with user's input"""
    global totalSearches
    global allSearchResults

    # ask user for regular expression to be searched
    expression = raw_input("Please enter the Regular Expression to be searched: "))
    print expression
    totalSearches += 1

    # perform regex search
    foundRegex = re.findall(expression, textFile)

    # if Regex search successful
    if len(foundRegex) != 0:
        print foundRegex

        # store result and search parameters in global 2D list
        if totalSearches == 1:
            allSearchResults[0] = [foundRegex, expression, totalSearches]
            print "Result has been stored. Its search number is 1."
        elif totalSearches == 21:
            print "I am sorry, but you have too many saved results to store another value."
        else:
            allSearchResults[totalSearches - 1] = [foundRegex, userParams[0], totalSearches]
            print "Result has been stored. Its search number is " + str(totalSearches)

    # if Regex search unsuccessful
    else:
        print "Search did not have any results."

    return

# One of the menu options. Will handle
# both querying user and searching for regex



def main_menu(textFile):
    """Main menu selection for user options in the script"""
    xFactor = True

    while xFactor:
        print "\n1- Enter new search string"
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
            return
        else:
            print "Not a valid response, please try again.\n"
            continue
    return

# This will be the central hub for the program.
# Will control when user decides to exit the program.


def search_past_result():
    """Search for prior result"""
    global allSearchResults

    # query user for what they want to search for
    while True:
        print "\nHow would you like to search for the prior result?"
        print "1- Search number"
        print "2- Search string"
        print "3- Search result"
        print "4- Exit to main menu"
        userInput = raw_input("Selection: ")

        # implement different search options

        # search for search number
        if userInput == "1":
            searchNumber = int(raw_input("Please input search number: "))
            for sublist in allSearchResults:
                if searchNumber == sublist[2]:
                    print sublist

        # search for search string
        elif userInput == "2":
            searchString = raw_input("Please input search string: ")
            for sublist in allSearchResults:
                if searchString == sublist[1]:
                    print sublist

        # search for past results
        elif userInput == "3":
            searchResult = raw_input("Please input search result: ")
            for sublist in allSearchResults:
                if searchResult == sublist[0]:
                    print sublist

        # exit to main menu
        elif userInput == "4":
            return

    # ask user if they want to search prior results again
        userInput = raw_input("Would you like find another prior result? (y/n): ").lower()
        if userInput == "n":
            return

    return


# This function is necessary.
# Need to decide how it returns the searched for result,
# and need to build error checking into the search

# Added more search options


def main():
    # Print initial greeting
    print "Hello, and welcome to 'Searching TheVerge'!."
    text = input_file()
    main_menu(text)
    return

# Have successfully simplified main() as much as possible

main()



# Ultimately, need to work out return sequence for values,
# which functions are necessary,
# and simplify the code where I can.
