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
    roman = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x",
             "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc", "c",
             "cc", "ccc", "cd", "d", "dc", "dcc", "dcc", "cm", "m"]
    decimal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    result = ""
    for i in range(len(decimal)-1, -1, -1):
        while number >= decimal[i]:
            number -= decimal[i]
            result += roman[i]
    return result

print(int_to_mini_roman(19))  # Output: 'xix'
print(int_to_mini_roman(152))  # Output: 'clii'
print(int_to_mini_roman(426))  # Output: 'cdxxvi'