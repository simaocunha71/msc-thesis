def sum_range_list(lst: list, start: int, end: int) -> int:
    return sum(lst[start:end+1])

print(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10))  # Output: 29


