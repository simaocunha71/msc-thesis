    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result


This code splits a string of parentheses into separate groups of balanced parentheses. It does this by iterating over the string, keeping track of the depth of the parentheses (number of open parentheses minus the number of closed parentheses). When it encounters a closed parenthesis at depth 0, it knows it's at the end of a group of balanced parentheses, so it adds the current string of parentheses to the result and clears the current string.


A: def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part  (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0


This code takes a floating point number and returns the decimal part of it. This is done by using the modulus operator (%). The modulus operator gives the remainder of the division of the two numbers. In this case, the number is divided by 1.0 (which is the decimal equivalent of 1), and the remainder (decimal part) is returned.


def is_bored(S):
    """
    You'll