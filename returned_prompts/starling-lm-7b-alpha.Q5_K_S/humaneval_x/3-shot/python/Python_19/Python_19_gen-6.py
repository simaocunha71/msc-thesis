    valid_numbers = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    numbers = [valid_numbers[num] for num in numbers.split()]

    numbers.sort()

    return ' '.join([str(num) for num in numbers])


