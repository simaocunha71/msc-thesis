    roman_numerals = {
        1: "i", 4: "iv", 5: "v", 9: "ix", 10: "x", 40: "xl", 50: "l",
        90: "xc", 100: "c", 400: "cd", 500: "d", 900: "cm", 1000: "m"
    }
    roman = ""
    i = 1000
    while i > 0:
        if number >= i:
            roman += roman_numerals[i]
            number -= i
        i //= 10
    return roman.lower()
