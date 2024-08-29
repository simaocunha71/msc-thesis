def is_polite(n: int):
    def is_power_of_two(n: int):
        return (n & (n - 1) == 0) and n != 0

    i = 1
    while n:
        if is_power_of_two(i):
            i *= 2
            continue
        n -= 1
        i += 1
    return i

print(is_polite(7)) # 11

#