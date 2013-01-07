# RegClass.py


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
