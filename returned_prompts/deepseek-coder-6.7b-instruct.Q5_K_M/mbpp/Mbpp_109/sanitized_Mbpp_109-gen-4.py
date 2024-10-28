def odd_Equivalent(binary,rotations):
    odd_count = 0
    binary = binary * rotations
    for i in range(rotations):
        rotated_binary = binary[i:] + binary[:i]
        if int(rotated_binary,2) % 2 == 1:
            odd_count += 1
    return odd_count