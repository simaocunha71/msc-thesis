def sum_in_range(l: int, r: int) -> int:
    odd_nums = [i for i in range(l, r+1) if i % 2 != 0]
    return sum(odd_nums)