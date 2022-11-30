#!/usr/bin/python3
def uppercase(string):
    string_new = ""
    for character in string:
        if ord(character) >= 97 and ord(character) <= 122:
            string_new += f"{ord(character) - 32:c}"
        else:
            string_new += f"{ord(character):c}"
    print("{:s}".format(string_new))
