
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
    mini_roman_numeral_map = (('m', 1000),
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
                              ('i', 1),
                              ('ixi', 9),
                              ('vii', 7),
                              ('ivi', 4),
                              ('ii', 2))
    result = ''
    for numeral, integer in mini_roman_numeral_map:
        count = number // integer
        result += numeral * count
        number -= integer * count
    return result
    """
    Function to convert integer to roman numeral
    """


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# ------------
# The code below is for the mini_roman_numeral_map which is not required in the question
# ------------

    mini_roman_numeral_map = (('m', 1000),
                              ('cm', 900),
                              ('d', 500),
                              ('cd', 400),
                              ('c', 100),
                              ('xc', 90),
                              ('l', 50),
                              ('xl', 4