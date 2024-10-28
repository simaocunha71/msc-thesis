    hex_to_decimal = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    count = 0
    for digit in num:
        if digit.isdigit() or digit.upper() in hex_to_decimal:
            if int(digit) == 2 or int(digit) == 3 or int(digit) == 5 or int(digit) == 7 or hex_to_decimal.get(digit.upper(), 0) in [11, 13]:
                count += 1
    return count
