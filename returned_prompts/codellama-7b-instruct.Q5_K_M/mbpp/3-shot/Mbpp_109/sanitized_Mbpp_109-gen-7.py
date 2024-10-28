def odd_Equivalent(binary_string, rotation_count):
    count = 0
    for i in range(rotation_count):
        binary_string = binary_string[-1] + binary_string[:-1]
        if int(binary_string, 2) % 2 == 1:
            count += 1
    return count