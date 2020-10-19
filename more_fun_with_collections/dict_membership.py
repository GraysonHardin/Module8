"""
Program: dict_membership.py
Author: Grayson Hardin
Last date modified: 10/19/2020
"""


def in_dict(values, search_term):
    results = search_term in values
    return results


if __name__ == '__main__':
    print(in_dict(values={'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}, search_term='A'))
    print(in_dict(values={'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}, search_term='G'))

