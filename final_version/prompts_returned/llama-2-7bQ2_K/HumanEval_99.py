
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

    # Function body
    def closest_integer(value):
        if '-' in value:
            if '.' in value:
                value, remainder = divmod(float(str(value)), 10)
            else:
                value, remainder = divmod(int(value), 10)

            if '.' not in value and -value != int(remainder):
                return round(value, 0)
        if value % 1 == 0:
            return value
        if (abs(value) > abs(int(str(value)) + str(min(1,-1))) and
           abs((-value)) < abs(-int(str(value)) + str(max(1, -1)))):
            return round((-abs(value)), 0)
        else:
            return value
    return closest_integer