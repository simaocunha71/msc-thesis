def odd_Equivalent(binary_string: str, num_rotations: int) -> int:
    odd_count = 0
    for i in range(num_rotations):
        if int(binary_string[-1]) % 2 != 0:
            odd_count += 1
        binary_string = binary_string[:-1] + binary_string[0]
    return odd_count