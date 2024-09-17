def odd_Equivalent(binary_string, n_rotations):
    binary_string = list(binary_string)
    for i in range(n_rotations):
        binary_string.append(binary_string.pop(0))
    count = 0
    for i in binary_string:
        if int(i) % 2 != 0:
            count += 1
    return count