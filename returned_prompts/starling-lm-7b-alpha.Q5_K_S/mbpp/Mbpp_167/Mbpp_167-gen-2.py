
def next_power_of_2(n: int) -> int:
    if n < 0:
        raise ValueError("The input should be a non-negative number")
    if n == 0:
        return 1
    return 2 ** (n.bit_length())


