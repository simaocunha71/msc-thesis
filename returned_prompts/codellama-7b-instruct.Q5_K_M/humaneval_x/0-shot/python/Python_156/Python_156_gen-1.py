
def int_to_mini_roman(number):
    if number == 1:
        return 'i'
    elif number == 4:
        return 'iv'
    elif number == 5:
        return 'v'
    elif number == 9:
        return 'ix'
    else:
        if number % 10 == 4:
            return int_to_mini_roman(number - 1) + 'iv'
        elif number % 10 == 9:
            return int_to_mini_roman(number - 1) + 'ix'
        else:
            return int_to_mini_roman(number // 10) + int_to_mini_roman(number % 10)

B:

def int_to_mini_roman(number):
    if number == 1:
        return 'i'
    elif number == 4:
        return 'iv'
    elif number == 5:
        return 'v'
    elif number == 9:
        return 'ix'
    else:
        return int_to_mini_roman(number // 10) + int_to_mini_roman(number % 10)

C:

def int_to_mini_roman(number):
    if number == 1:
        return 'i'
    elif number == 4:
        return 'iv'
    elif number == 5:
        return 'v'
    elif number == 9:
        return 'ix'
    else:
        return int_to_mini_roman(number // 10) + int_to_mini_roman(number % 10)

D:

def int_to_mini_roman(number):
    if number == 1:
        return 'i'
    elif number == 4:
        return 'iv'
    elif number == 5:
        return 'v'
    elif number == 9:
        return 'ix'
    else:
        return int_to_mini_roman(number // 10) + int