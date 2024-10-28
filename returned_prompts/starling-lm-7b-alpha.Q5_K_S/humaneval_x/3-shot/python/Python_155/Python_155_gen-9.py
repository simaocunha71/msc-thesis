    count_odd = 0
    count_even = 0
    num = abs(num)
    while num > 0:
        d = num % 10
        if d % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        num //= 10
    return count_odd, count_even


