"""
Program: scores.py
Author: Grayson Hardin
Last date modified: 10/19/2020

The program accepts a number of tests taken, the score received for each test, and then returns the average.
"""


def get_test_score():
    score_dict = dict()

    num_scores = int(input("Enter the number of tests taken: "))  # Gain the input for x number of tests taken
    if num_scores < 0:  # Raise an error if invalid input
        raise ValueError

    for i in range(num_scores):
        score = int(input("Enter the score of test: "))
        if score < 0:  # Raise an error if invalid input
            raise ValueError
        score_dict.update({f'test{i + 1}': score})

    return score_dict


def average_scores(scores):
    values = scores.values()
    return sum(values) / len(values)  # The calculation process


def main():
    get_scores = get_test_score()
    get_average = average_scores(scores=get_scores)
    print(get_average)


if __name__ == '__main__':
    main()
