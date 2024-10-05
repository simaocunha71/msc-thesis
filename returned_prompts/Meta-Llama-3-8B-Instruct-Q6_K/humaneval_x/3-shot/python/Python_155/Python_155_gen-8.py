    even_count = 0
    odd_count = 0

    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return (even_count, odd_count) if num >= 0 else (odd_count, even_count)  # adjust for negative numbers


