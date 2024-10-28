    roman = ""
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]

    for i in range(len(values)):
        count = int(number / values[i])
        roman += symbols[i] * count
        number -= values[i] * count

    return roman

