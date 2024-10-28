    def roman_numeral_helper(number, symbols):
        if number < 0:
            return None
        if number == 0:
            return ""
        if number < 10:
            return symbols[number]
        else:
            return roman_numeral_helper(number // 10, symbols[10:]) + symbols[number % 10]

    symbols = [0, "m", "mm", "mmm", "m", "cm", "cc", "c",
               "xc", "xl", "x", "l", "xl", "xc", "xc", "c",
               "xc", "mc", "mc", "mm", "m", "cd", "d", "dc", "d",
               "cd", "cm", "cc", "c", "xc", "lc", "lc", "l", "xl", "xc",
               "xc", "mc", "mc", "mm", "m", "xcd", "d", "dc", "d", "cd",
               "cd", "cm", "cc", "c", "xc", "lc", "lc", "l", "xl", "xc",
               "xc", "mc", "mc", "mm", "m", "xc", "mc", "mc", "mm", "m", "cm",
               "cc", "c", "xc", "lc", "lc", "l", "xl", "xc", "xc", "mc", "mc",
               "mm", "m", "xcd", "d", "dc", "d", "cd", "cd", "cm", "cc", "c"]

    return roman_numeral_helper(number, symbols)


