    count = 0
    for n in arr:
        sum_of_digits = 0
        if n < 0:
            n *= -1
        while n > 0:
            sum_of_digits += n % 10
            n //= 10
        if sum_of_digits > 0:
            count += 1
    return count


