def odd_Equivalent(binary_string, rotation_times):
    rotated_string = (binary_string * 2)[rotation_times:]
    count = 0
    for i in range(len(binary_string)):
        if int(rotated_string[i:i+len(binary_string)], 2) % 2 != 0:
            count += 1
    return count