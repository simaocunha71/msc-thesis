    roman_numerals = ['m', 'cm', 'd', 'cd', 'c', 'x', 'xl', 'l', 'xci', 'v', 'iv', 'i']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    result = ''
    while number > 0:
        for i, v in enumerate(values):
            if number >= v:
                number -= v
                result += roman_numerals[i]
                break

    return result


