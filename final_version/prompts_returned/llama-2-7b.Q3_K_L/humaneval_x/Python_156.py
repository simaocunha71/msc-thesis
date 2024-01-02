
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    
    roman = []
    while number > 0:
        while number % 1000 == 0:
            roman += ['M']
            number -= 1000
        if number % 1000 == 999:
            roman += [roman[-1] * int(number / 1000)]
            number = 0
        elif number % 1000 >= 500:
            roman += ['D']
        else:
            roman += [roman[-1] + 'C' if (number % 100 == 4) else 'C']
            number -= 99
    return "".join(roman).lower()