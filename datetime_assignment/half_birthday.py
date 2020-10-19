"""
Program: half_birthday.py
Author: Grayson Hardin
Last date modified: 10/19/2020

Program returns the date for half birthday.
"""


import datetime


def half_birthday(birthday):
    return birthday + datetime.timedelta(days=365 / 2)  # This will calculate the date


def main():
    new_half_birthdate = half_birthday(birthday=datetime.date(2020, 7, 15))  # Function called and assigned last birthday.
    print(new_half_birthdate)


if __name__ == '__main__':
    main()
