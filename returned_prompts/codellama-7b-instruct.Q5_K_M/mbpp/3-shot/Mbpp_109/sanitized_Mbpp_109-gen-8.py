def odd_Equivalent(binary_string: str, n: int) -> int:
    total_odd = 0
    for i in range(n):
        binary_string = binary_string[1:] + binary_string[0]
        if int(binary_string, 2) % 2 != 0:
            total_odd += 1
    return total_odd