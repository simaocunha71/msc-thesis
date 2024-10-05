    num = str(abs(num))
    even_count = sum(1 for digit in num if int(digit) % 2 == 0)
    odd_count = sum(1 for digit in num if int(digit) % 2 != 0)
    return (even_count, odd_count)


