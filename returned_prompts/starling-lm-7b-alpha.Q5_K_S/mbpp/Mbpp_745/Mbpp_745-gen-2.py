
def divisible_by_digits(startnum, endnum):
    return [i for i in range(startnum, endnum + 1) if all(i % j == 0 for j in map(int, str(i)))]


