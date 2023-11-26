

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Convert number to int
    if not number:
        return 0.0
    else:
        number = str(number)
        int_part, decimals = number[:], number[1:]
        # Check for negative values
        if int_part[-1] == '-':
            number = int_part[:-2] + '-' + int_part[0:4]
        else:
            number = str(int_part)
        return float(number) / 10 ** decimals
