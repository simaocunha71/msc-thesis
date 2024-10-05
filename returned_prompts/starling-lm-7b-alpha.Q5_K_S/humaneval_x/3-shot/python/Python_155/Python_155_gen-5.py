    count_odd = 0
    count_even = 0

    while num > 0:
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        num //= 10
    return count_odd, count_even


