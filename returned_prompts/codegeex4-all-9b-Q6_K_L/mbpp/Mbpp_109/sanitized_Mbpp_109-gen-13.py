def odd_Equivalent(binary_string: str, rotations: int) -> int:
    odd_count = 0
    for _ in range(rotations):
        if binary_string[-1] == '1':
            odd_count += 1
        binary_string = binary_string[:-1] + binary_string[0]
    return odd_count