
def closest_integer(value):
    """
    Find the closest integer to the given value.
    If the value is equidistant between two integers,
    return the one that is away from zero.
    :param value: string representing a number
    :return: int
    """
    # convert the input to a float
    number = float(value)
    # round the number to the nearest integer
    rounded = round(number)
    # if the rounded number is equidistant from two integers,
    # return the one away from zero
    if abs(rounded - number) == 0.5:
        return 1 if rounded > 0 else -1
    # otherwise, return the rounded number
    return rounded
