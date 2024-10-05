    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, float) and isinstance(b, float):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, str) and isinstance(b, str):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    else:
        raise TypeError


def compare_two(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_two(1, 2.5) ➞ 2.5
    compare_two(1, "2,3") ➞ "2,3"
    compare_two("5,1", "6") ➞ "6"
    compare_two("1", 1) ➞ None
    """

    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, float) and isinstance(b, float):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif isinstance(a, str) and isinstance(b, str):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    else:
        raise TypeError


def compare_three(a, b, c):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the largest variable in its given variable type.
    Return None if the values