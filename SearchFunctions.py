# SearchFunctions.py

import re

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

#######################################################################


def search_past_results():
    """Search for prior results"""
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

# Could implement functionality to print result to file
# and need to build error checking into the search
