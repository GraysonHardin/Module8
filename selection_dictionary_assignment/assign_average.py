def switch_average(key):
    dictionary = {
        'A': [5, 10, 15, 20],

    }

    try:
        values = dictionary.get(key)
        return calculate_average(values)

    except:
        raise ValueError


def calculate_average(values):
    return sum(values) / len(values)


def main():
    user_input = input('Enter value A-D: ')
    average = switch_average(key=user_input)
    print(average)


if __name__ == '__main__':
    main()
