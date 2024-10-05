    count_even = 0
    count_odd = 0

    while num > 0:
        if num % 10 == 0:
            count_even += 1
        else:
            count_odd += 1

        num //= 10

    return count_even, count_odd


