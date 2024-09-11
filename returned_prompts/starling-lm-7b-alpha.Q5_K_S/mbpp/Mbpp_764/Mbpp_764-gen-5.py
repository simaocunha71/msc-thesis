"""
def number_ctr(input_string):
    """
    Count the number of digits in a given string
    """
    digit_count = 0
    for char in input_string:
        if char.isdigit():
            digit_count += 1
    return digit_count


assert number_ctr('program2bedone') == 1
"""

number_ctr = lambda input_string: sum(1 for char in input_string if char.isdigit())
assert number_ctr('program2bedone') == 1

def number_ctr(input_string):
    """
    Count the number of digits in a given string
    """
    digit_count = 0
    for char in input_string:
        if char.isdigit():
            digit_count += 1
    return digit_count


assert number_ctr('program2bedone') == 1


def number_ctr(input_string):
    """
    Count the number of digits in a given string
    """
    return sum(1 for char in input_string if char.isdigit())


assert number_ctr('program2bedone') == 1

def number_ctr(input_string):
    """
    Count the number of digits in a given string
    """
    return len([char for char in input_string if char.isdigit()])

assert number_ctr('program2bedone') == 1


def number_ctr(input_string):
    """
    Count the number of digits in a given string
    """
    return len([char for char in input_string if char.isdigit()])

assert number_ctr('program2bedone') == 1

def number_ctr(input_string):
    """
    Count the number of digits in a given string
    """
    return input_string.count('0') + input_string.count('1') + input_string.count('2') + \
           input_string.count('3') + input_string.count('4') + input_string.count('5') + \
           input_string.count('6') + input_string.