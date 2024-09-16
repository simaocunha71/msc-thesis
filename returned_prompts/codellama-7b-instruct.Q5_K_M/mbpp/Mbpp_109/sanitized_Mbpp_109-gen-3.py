def odd_Equivalent(binary_string,rotations):
    binary_string = binary_string[rotations:] + binary_string[:rotations]
    return binary_string.count("1")