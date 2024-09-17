def first_Digit(n):
    if not isinstance(n, int):
        return "Error: Input is not an integer"
    n = abs(n)
    return int(str(n)[0])