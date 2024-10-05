    count_odd = 0
    count_even = 0
    while num > 0:
        last_digit = num % 10
        if last_digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        num = num // 10
    return (count_even, count_odd)


