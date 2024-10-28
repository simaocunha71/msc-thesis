def first_Digit(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    if n < 0:
        n = -n
    return int(str(n)[0])