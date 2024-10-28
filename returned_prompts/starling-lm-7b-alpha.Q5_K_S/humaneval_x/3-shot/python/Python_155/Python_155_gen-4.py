    count_even, count_odd = 0, 0

    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

        num //= 10

    return count_even, count_odd


