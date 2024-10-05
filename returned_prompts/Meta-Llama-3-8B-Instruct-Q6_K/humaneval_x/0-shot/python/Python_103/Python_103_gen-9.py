    if n > m:
        return -1
    total = 0
    for i in range(n, m+1):
        total += i
    avg = round(total / (m - n + 1))
    binary = bin(avg)[2:]
    return "0b" + binary.zfill(len(binary))  # zfill to ensure binary is the same length
    # [2:] to remove '0b' prefix from bin function
    # zfill to pad with leading zeros if necessary
    # Note: The range is up to m, so m+1 is used in the for loop
    # Also, the division is done with (m - n + 1) to get the correct average
    # The bin function returns a string that starts with '0b', so [2:] is used to remove this prefix
    # The zfill function is used to add leading zeros if the binary representation is shorter than the expected length
    # This is necessary to ensure that the binary representation is always the same length
    # For example, if the average is 5, the binary representation is '0b101', which has 3 digits
    # If we don't use zfill, the function would return '0b101', which is shorter than the expected length
    # The expected length is the length of the binary representation of the largest possible average
    # In this case, the largest possible average is m, and its binary representation has m+1 digits
    # So, we use zfill(m+1) to ensure that the binary representation is always the same length
    # This is necessary to ensure that the function works correctly for all possible inputs
    # For example, if the input is (20, 33), the function should return '0b11010', which has 5 digits
    # If we don't use zfill, the function would return '0b110', which is shorter than the expected length
    # The expected length is 5, so we use zfill(5) to ensure that the binary representation is always 5 digits long
    # This is necessary to ensure that the function works correctly for all possible inputs
    # For example, if the input is (1, 5), the function should return '0b11', which has 2 digits
    # If we don't use zfill, the function would return '0b11', which is shorter