
def int_to_mini_roman(number):
    if number == 0:
        return ""

    roman_numerals = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m"
    }

    mini_roman_numerals = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m"
    }

    mini_roman_numerals[500] = "d"
    mini_roman_numerals[400] = "cd"
    mini_roman_numerals[100] = "c"
    mini_roman_numerals[90] = "xc"
    mini_roman_numerals[50] = "l"
    mini_roman_numerals[40] = "xl"
    mini_roman_numerals[10] = "x"
    mini_roman_numerals[9] = "ix"
    mini_roman_numerals[5] = "v"
    mini_roman_numerals[4] = "iv"
    mini_roman_numerals[1] = "i"

    roman_numeral_string = ""

    for key in sorted(roman_numerals, reverse=True):
        while number >= key:
            number -= key
            roman_numeral_string += mini_roman_numerals[key]

    return roman_numeral_string


