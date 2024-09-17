def find_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    lucas_numbers = [2, 1]
    for i in range(2, n + 1):
        lucas_numbers.append(lucas_numbers[i - 1] + lucas_numbers[i - 2])
    return lucas_numbers[n]