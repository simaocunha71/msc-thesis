def odd_Equivalent(binary_string: str, rotations: int) -> int:
    count = 0
    for i in range(rotations):
        if binary_string[-1] == '1':
            count += 1
        binary_string = binary_string[:-1] + binary_string[0]
    return count