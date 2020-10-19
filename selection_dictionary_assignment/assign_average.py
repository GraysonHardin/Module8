"""
Program: assign_average.py
Author: Grayson Hardin
Last date modified: 10/19/2020

This program will take a key and store a list of values within that key. The user will then be prompted to enter a key (A-D) and the program will return the average of the values.
"""


def switch_average(key):  # The four keys and their values
    dictionary = {
        'A': [5, 10, 15, 20],
        'B': [10, 20, 30, 40, 50],
        'C': [1, 2, 3],
        'D': [5]
    }

    try:  # Try/Catch to handle bad input
        values = dictionary.get(key)
        return calculate_average(values)

    except:
        raise ValueError


def calculate_average(values):  # This function provides the logic for calculating the average
    return sum(values) / len(values)


def main():  # This function grabs the user input
    user_input = input('Enter a letter from A-D: ')
    average = switch_average(key=user_input)
    print(average)


if __name__ == '__main__':
    main()
