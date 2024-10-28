def odd_Equivalent(binary_string, times):
    rotated_string = binary_string[len(binary_string) - times:] + binary_string[:len(binary_string) - times]
    count = 0
    for i in rotated_string:
        if int(i) % 2 != 0:
            count += 1
    return count