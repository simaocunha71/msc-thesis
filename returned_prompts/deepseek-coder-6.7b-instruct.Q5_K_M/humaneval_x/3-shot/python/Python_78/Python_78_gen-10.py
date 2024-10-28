    primes = [2, 3, 5, 7, 11, 13]
    hex_nums = "0123456789ABCDEF"
    count = 0
    for i in num:
        if int(i, 16) in primes:
            count += 1
    return count


