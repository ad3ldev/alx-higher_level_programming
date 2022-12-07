#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)
        
    string = roman_string.upper()
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }    
    num = 0

    for i in range(len(string)):
        if i!= len(string)-1 and roman[string[i]] < roman[string[i+1]]:
            num += roman[string[i]]*-1
        else:
            num += roman[string[i]]

    return num