    num = str(abs(num))  # Convert the number to a string to iterate over its digits.
    even_count = 0
    odd_count = 0

    for digit in num:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count)


