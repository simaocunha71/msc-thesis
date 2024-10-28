

def greatest_common_divisor(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


if __name__ == "__main__":
    import doctest
    doctest.testmod()

