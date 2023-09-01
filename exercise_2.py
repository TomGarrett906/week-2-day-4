#Exercise 2 - Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case

class String:

    def __init__(self, string):
        self.string = ''
        self.string = string
        
    def get_string(self):
        self.string = input("Enter any string: ").upper()
        return self.string

    def print_string(self):    
        print(self.string)

user_string = String('')
user_string.get_string()
user_string.print_string()