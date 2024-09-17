def highest_Power_of_2(n: int) -> int:
    return 2**(n.bit_length()-1) if n and (n & (n-1)) == 0 else 0