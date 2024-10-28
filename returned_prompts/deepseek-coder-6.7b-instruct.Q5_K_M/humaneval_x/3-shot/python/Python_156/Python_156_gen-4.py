    roman_numeral_map = (('m', 1000),
                         ('cm', 900),
                         ('d', 500),
                         ('cd', 400),
                         ('c', 100),
                         ('xc', 90),
                         ('l', 50),
                         ('xl', 40),
                         ('x', 10),
                         ('ix', 9),
                         ('v', 5),
                         ('iv', 4),
                         ('i', 1))

    result = ""
    for numeral, integer in roman_numeral_map:
        count = number // integer
        result += numeral * count
        number -= integer * count
    return result


