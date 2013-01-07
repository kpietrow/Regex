# Kevin Pietrow
# Regex searching on large text file

import os
from RegClass import Reg_Search            # Class for storing results
from SearchFunctions import new_search_regex, search_past_results

# set up global array for storing results
allSearchResults = []

# set up global counter for amount of searches
totalSearches = 0

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



def main_menu(textFile):
    """Main menu for user options in the script"""
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
            search_past_results()
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


def main():
    # Print initial greeting
    print "Hello, and welcome to The Regex() Searcher!"
    text = input_file()            # Call function to obtain search file
    main_menu(text)                # Call the main menu function
    return

# Have successfully simplified main() as much as possible

main()



