def odd_Equivalent(binary_string, rotations: int) -> int:
    count = 0
    for i in range(rotations):
        binary_string = binary_string[-1] + binary_string[:-1]
        if int(binary_string, 2) % 2 == 1:
            count += 1
    return count
