# Kevin Pietrow
# Regex searching on large text file

import re
import sys
import os

# set up global array for storing results
allSearchResults = []

# set up global counter for amount of searches
totalSearches = 0


# Class for searches
class Reg_Search(object):

    def __init__(self, search_number, expression, result):
        self.search_number = search_number         # Global search number
        self.expression = expression               # Regular expression searched
        self.result = str(result)                  # Result of regex() search
                                                   # Convert to string for easier use later

    def display_search(self):
        # prints out object information
        print "\nSearch number: " + str(self.search_number) + "\nExpression searched: " + str(self.expression) + "\nResult: " + str(self.result) + "\n"


def input_file():
    """Open file"""
    textFile = raw_input("What file would you like to search?: ")        # Query user for filename

    # Attempt to open file
    while True:
        try:
            rt = open(os.path.abspath(textFile), 'r')                    # Use os.* to search user's machine

        # Catch nonexistent file error
        except IOError:
            print "Failure to locate file."
            textFile = raw_input("Please enter a different file: ")      # Query for new file
            continue

        else:
            break

    text = rt.read()
    print "Successfully loaded the file!"
    return text

# Necessary code. This opens up the text file that the user requested.
# Acceptable error checking


def new_search_regex(textFile):
    """Query for input, then performs RegEx() with user's input"""
    global totalSearches
    global allSearchResults

    # perform initial regex search
    while 1:
        try:
            # ask user for regular expression to be searched
            expression = raw_input("Please enter the Regular Expression to be searched: ")
            foundRegex = re.search(expression, textFile)
        except sre_constants.error:
            print "Bad character range for the Regular Expression. Please try another"
            continue
        else:
            break


    # if Regex search successful
    if foundRegex != None:

        # Do complete regex search
        foundRegex = re.findall(expression, textFile)

        # Print result
        print "Result: " + str(foundRegex)

        # Increment global total
        totalSearches += 1

        # create object for result, store in global array
        reg_object = Reg_Search(totalSearches, expression, foundRegex)
        allSearchResults.append(reg_object)
        print "You're search number for this search is " + str(totalSearches)    # Inform user of storage location

    # if Regex search unsuccessful
    else:
        print "Search did not have any results."

    return

# One of the menu options. Will handle
# both querying user for expression, and searching for regex



def main_menu(textFile):
    """Main menu selection for user options in the script"""
    xFactor = True

    while xFactor:
        print "\n1- Enter new search string"
        print "2- Access prior search result"
        print "3- Display loaded file"
        print "4- Exit program"
        userInstr = raw_input("Selection: ")

        # Call different functions depending on user input
        # Call searcher function
        if userInstr == "1":
            print ""
            new_search_regex(textFile)
        # Call past result function
        elif userInstr == "2":
            print ""
            search_past_result()
        # Display text to be searched
        elif userInstr == "3":
            print textFile + "\n"
        # Exit program
        elif userInstr == "4":
            print "Exiting program now."
            return
        # If invalid response
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
        print "2- Search expression"
        print "3- Search result"
        print "4- Exit to main menu"
        userInput = raw_input("Selection: ")

        # implement different search options

        # search for search number
        if userInput == "1":
            search = int(raw_input("\nPlease input search number: "))
            try:
                allSearchResults[search - 1].display_search()
            except IndexError:
                print "Could not locate data. Please try different search criteria."
                continue

        # query for search expression
        elif userInput == "2":
            unsuccessful = True
            search = raw_input("\nPlease input expression: ")     # Query user for expression to search for
            for item in allSearchResults:                         # Runs through global array
                if search == item.expression:                     # If a match for object property
                    item.display_search()                         # Display object
                    unsuccessful = False

            if unsuccessful:
                print "Could not locate data. Please try different search criteria."
                continue

        # query for search result
        elif userInput == "3":
            unsuccessful = True
            search = raw_input("\nPlease input search result: ")
            for item in allSearchResults:
                if search == item.result:
                    item.display_search()
                    unsuccessful = False

            if unsuccessful:
                print "Could not locate data. Please try different search criteria."
                continue

        # Note: this section is broken. Must determine how to effectively
        # search for the result criteria

        # exit to main menu
        elif userInput == "4":
            return

        else:
            continue

    # ask user if they want to search prior results again
        while True:
            userInput = raw_input("Would you like find another prior result? (y/n): ").lower()
            if userInput == "n":
                return
            elif userInput == "y":
                break
            else:
                print "Error. Invalid response. Please try again"

    return


# This function is necessary.
# Call a display function in the Reg_Search class to display results
# Could implement functionality to print result to file
# and need to build error checking into the search

# Added more search options


def main():
    # Print initial greeting
    print "Hello, and welcome to The Regex() Searcher!"
    text = input_file()            # Call function to obtain search file
    main_menu(text)                # Call the main menu function
    return

# Have successfully simplified main() as much as possible

main()


# Also, past search section needs work
# Need to figure out how to keep these as persistent values
# ^ sqlite may be the answer
