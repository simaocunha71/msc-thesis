

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # if number is already a whole number, return it as it is
    if abs(number - int(number)) < 0.01:
        return number
    # otherwise, get the integer part and the decimals
    (integer_part, decimal) = divmod(number, 1.)
    return decimal
