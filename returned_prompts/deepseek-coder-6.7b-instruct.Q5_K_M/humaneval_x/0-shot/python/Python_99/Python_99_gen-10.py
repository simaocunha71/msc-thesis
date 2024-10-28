
    import math
    def closest_integer(value):
        '''
        Create a function that takes a value (string) representing a number
        and returns the closest integer to it. If the number is equidistant
        from two integers, round it away from zero.

        Examples
        >>> closest_integer("10")
        10
        >>> closest_integer("15.3")
        15

        Note:
        Rounding away from zero means that if the given number is equidistant
        from two integers, the one you should return is the one that is the
        farthest from zero. For example closest_integer("14.5") should
        return 15 and closest_integer("-14.5") should return -15.
        '''
        num = float(value)
        if num > 0:
            return math.floor(num + 0.5)
        else:
            return math.ceil(num - 0.5)

    print(closest_integer("10"))
    print(closest_integer("15.3"))
    print(closest_integer("14.5"))
    print(closest_integer("-14.5"))

    '''
    This function works by first converting the input string to a float.
    It then uses the math library's floor() and ceil() functions to find the
    closest integer to the input number. If the number is positive, floor() is
    used to round down to the nearest integer. If the number is negative,
    ceil() is used to round up to the nearest integer.

    The 0.5 is added or subtracted from the number before the rounding is
    performed to handle the case where the input number is exactly halfway
    between two integers. In this case, rounding away from zero is performed,
    which means the number is rounded to the integer that is farthest from zero.
    '''

    '''
    Here, the float() function is used to convert the input string to a float.
    If the number is positive, the math.floor() function is used to round down
    to the nearest integer. If the number is negative, the math.ceil() function
    is used to round up