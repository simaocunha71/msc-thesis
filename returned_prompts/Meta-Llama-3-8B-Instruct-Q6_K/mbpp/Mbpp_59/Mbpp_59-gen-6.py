def is_octagonal(n):
    octagonal_nums = []
    octagonal_num = 1
    while True:
        octagonal_num += 8 * (n - 1) + 1
        octagonal_nums.append(octagonal_num)
        n -= 1
        if n == 0:
            break
    return octagonal_nums[-1]
print(is_octagonal(5)) # Output: 65

