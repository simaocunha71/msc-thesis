def sum_in_range(l: int, r: int) -> int:
    sum = 0
    for i in range(l, r+1, 2):
        sum += i
    return sum