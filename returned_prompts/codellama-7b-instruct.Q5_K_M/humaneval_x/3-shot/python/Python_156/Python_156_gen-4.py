    if number <= 9:
        return str(number)
    elif number == 10:
        return 'x'
    elif number == 50:
        return 'l'
    elif number == 90:
        return 'xc'
    elif number == 400:
        return 'cd'
    elif number == 900:
        return 'cm'
    else:
        return ''.join([int_to_mini_roman(number // 10) + int_to_mini_roman(number % 10)])


