def next_power_of_2(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    return 1 << (n - 1).bit_length()

