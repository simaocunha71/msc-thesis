
def next_power_of_2(n: int) -> int:
    return 2 ** (n.bit_length())


