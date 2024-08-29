def pancake_sort(lst: list) -> list:
    n = len(lst)
    for i in range(n):
        max_idx = max_element(lst, 0, n-i)
        lst = flip(lst, max_idx)
        lst = flip(lst, n-i-1)
    return lst
def max_element(lst: list, start: int, end: int) -> int:
    max_idx = start
    for i in range(start, end):
        if lst[i] > lst[max_idx]:
            max_idx = i
    return max_idx
def flip(lst: list, end: int) -> list:
    start = 0
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst