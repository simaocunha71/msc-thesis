
def next_power_of_2(n:int):
    if n < 0:
        return 0
    else:
        return 2 ** (n.bit_length())


