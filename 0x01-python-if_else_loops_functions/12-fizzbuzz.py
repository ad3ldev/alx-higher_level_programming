#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        string = ""
        if (number % 3 == 0):
            string += "Fizz"
        if (number % 5 == 0):
            string += "Buzz"
        if (string != ""):
            print(string, end=' ')
        else:
            print(number, end=' ')
