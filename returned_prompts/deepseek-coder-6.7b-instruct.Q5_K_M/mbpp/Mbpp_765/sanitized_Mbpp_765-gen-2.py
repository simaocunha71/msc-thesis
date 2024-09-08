def is_polite(n):
    def is_power_of_two(n):
        return (n and (not(n & (n - 1))))
 
    i = 1
    while n:
        if is_power_of_two(i):
            i *= 2
            continue
        n -= 1
        i += 1
    return i//2