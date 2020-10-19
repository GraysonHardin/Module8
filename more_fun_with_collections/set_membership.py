"""
Program: set_membership.py
Author: Grayson Hardin
Last date modified: 10/19/2020

The program is designed to accept a list of values, search for an item, and then print to the console whether the output is true or false.
"""


def in_set(values, search_term):
    results = search_term in values  # This will take search_term and locate whether it is within the stored values.
    return results


if __name__ == '__main__':
    print(in_set(values={1, 2, 3, 4, 5}, search_term=5))  # Both lines 7 and 8 are examples that can be modified.
    print(in_set(values={1, 2, 3, 4, 5}, search_term=6))
